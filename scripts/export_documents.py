"""Export writing to Word. Requires python-docx. Review copies use the private
Site until a public_experience_url is configured. Portable reading pages use
relative links and work when extracted alongside index.html.
"""
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from build_publication import ROOT, CONFIG, INLINE, blocks, render_markdown

def add_inline(paragraph, text, bold=False, italic=False):
    end=0
    def run(value, strong=bold, emphasis=italic):
        r=paragraph.add_run(value);r.bold=strong;r.italic=emphasis
        return r
    for match in INLINE.finditer(text):
        if match.start()>end: run(text[end:match.start()])
        if match.group(1) is not None:
            link=OxmlElement('w:hyperlink')
            link.set(qn('r:id'),paragraph.part.relate_to(match.group(2),RT.HYPERLINK,is_external=True))
            r=OxmlElement('w:r');pr=OxmlElement('w:rPr')
            color=OxmlElement('w:color');color.set(qn('w:val'),'086477');pr.append(color)
            underline=OxmlElement('w:u');underline.set(qn('w:val'),'single');pr.append(underline)
            if bold: pr.append(OxmlElement('w:b'))
            r.append(pr);t=OxmlElement('w:t');t.text=match.group(1);r.append(t);link.append(r)
            paragraph._p.append(link)
        elif match.group(3) is not None:
            add_inline(paragraph,match.group(3),bold=True,italic=italic)
        else:
            run(match.group(4),emphasis=True)
        end=match.end()
    if end<len(text):run(text[end:])

def make_docx(name):
    doc=Document();section=doc.sections[0]
    section.page_width=Inches(8.5);section.page_height=Inches(11)
    section.top_margin=Inches(.75);section.bottom_margin=Inches(.75)
    section.left_margin=Inches(.85);section.right_margin=Inches(.85)
    normal=doc.styles['Normal'];normal.font.name='Cambria';normal.font.size=Pt(11)
    normal.paragraph_format.line_spacing=1.13
    normal.paragraph_format.space_after=Pt(8)
    normal.paragraph_format.widow_control=True
    for style_name,size in [('Title',26),('Subtitle',15),('Heading 1',15),('Heading 2',12)]:
        style=doc.styles[style_name];style.font.name='Calibri';style.font.size=Pt(size)
        style.font.color.rgb=RGBColor(0,0,0)
        style.paragraph_format.space_before=Pt(15 if style_name.startswith('Heading') else 0)
        style.paragraph_format.space_after=Pt(9)
        style.paragraph_format.keep_with_next=True
    doc.styles['Title'].font.bold=True
    doc.styles['Subtitle'].font.italic=False
    for border in doc.styles.element.xpath('.//w:pBdr'):
        border.getparent().remove(border)
    doc.core_properties.author=CONFIG['author'];doc.core_properties.title=CONFIG['title']
    doc.core_properties.subject='Workarounds and decision rights in AI systems'
    doc.core_properties.keywords='AI agents, delegation, authority, evidence'
    footer=section.footer.paragraphs[0];footer.alignment=2
    field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
    destination=CONFIG.get('public_experience_url') or CONFIG['review_experience_url']
    text=render_markdown(name,destination)
    reference_mode=False
    for kind,value in blocks(text):
        if kind=='h1':doc.add_paragraph(value,'Title')
        elif kind=='h2':doc.add_paragraph(value,'Subtitle')
        elif kind.startswith('h'):
            p=doc.add_paragraph(value,'Heading 1')
            if value in ['References','Sources']:
                p.paragraph_format.page_break_before=True;reference_mode=True
            elif value=='Source and method note':reference_mode=False
        elif kind=='table':
            table=doc.add_table(rows=0,cols=len(value[0]));table.alignment=WD_TABLE_ALIGNMENT.CENTER;table.autofit=False
            for col,width in zip(table.columns,[1.35,3.15,2.3]):col.width=Inches(width)
            for idx,rowdata in enumerate(value):
                row=table.add_row()
                pr=row._tr.get_or_add_trPr();pr.append(OxmlElement('w:cantSplit'))
                if idx==0:pr.append(OxmlElement('w:tblHeader'))
                for cell,content,width in zip(row.cells,rowdata,[1.35,3.15,2.3]):
                    cell.width=Inches(width);cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
                    p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(6);p.paragraph_format.space_before=Pt(6)
                    r=p.add_run(content);r.font.name='Calibri';r.font.size=Pt(10);r.bold=idx==0
                    if idx==0:
                        shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'E6EDEF');cell._tc.get_or_add_tcPr().append(shade)
            doc.add_paragraph().paragraph_format.space_after=Pt(2)
        else:
            p=doc.add_paragraph();add_inline(p,value)
            if value==CONFIG['author']:
                p.paragraph_format.space_after=Pt(20)
                for r in p.runs:r.font.name='Calibri';r.font.size=Pt(10)
            if value.startswith('**['):
                p.paragraph_format.space_before=Pt(5);p.paragraph_format.space_after=Pt(13)
            if reference_mode and value.startswith('OpenAI.'):
                p.paragraph_format.left_indent=Inches(.3);p.paragraph_format.first_line_indent=Inches(-.3)
                p.paragraph_format.keep_together=True
    target=ROOT/'publishing'/f'Who_Gave_the_Agent_That_Authority_{name.title()}_Christopher_Hayes.docx'
    doc.save(target)
    print(target)

if __name__=='__main__':
    for name in ['essay','substack']:make_docx(name)
