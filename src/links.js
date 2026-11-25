// Stable, host-independent editorial entry points; unknown fragments remain harmless.
let linkedCaseDialog=false;
function momentURL(fragment){const url=new URL(location.href);url.search='';url.hash=fragment;return url.href}
async function copyEditorialLink(fragment,statusId,fallbackId){
 const url=momentURL(fragment),statusNode=$(statusId),fallback=$(fallbackId);
 try{if(!navigator.clipboard?.writeText)throw new Error('Clipboard unavailable');await navigator.clipboard.writeText(url);statusNode.textContent='Link copied.';fallback.hidden=true}
 catch{fallback.value=url;fallback.hidden=false;fallback.focus();fallback.select();statusNode.textContent='The link is selected below for copying.'}
}
function openEditorialMoment(){
 let fragment;try{fragment=decodeURIComponent(location.hash.slice(1))}catch{return}
 if(linkedCaseDialog&&$('case-dialog').open)$('case-dialog').close();linkedCaseDialog=false;storyLinkPin=null;
 const moment=DATA.moments.find(m=>m.id===fragment),caseMatch=/^case-([RN]\d{3})$/.exec(fragment);
 if(!moment&&!(caseMatch&&C[caseMatch[1]]))return;
 filter='All';query='';$('search').value='';
 const caseId=moment?.case||caseMatch[1];branchTheme=C[caseId].boundary;
 if(moment?.view)atlasMode=moment.view;
 if(moment?.compare)compareId=moment.compare;
 renderFilters();choose(caseId);
 if(moment?.compare){$('case-compare').open=true;renderComparison()}
 if(Number.isInteger(moment?.story)){setStory(moment.story);storyLinkPin=moment.story}
 let target=moment?$(moment.target):$('atlas');
 if(moment?.story!==undefined&&innerWidth<900)target=$('workbook-scene');
 if(!target)return;
 requestAnimationFrame(()=>{
  if(moment?.view==='authority'){
   const row=document.querySelector(`#authority-body [data-select="${caseId}"]`)?.closest('tr'),scroller=document.querySelector('.authority-scroll');
   if(row&&scroller)scroller.scrollTop+=row.getBoundingClientRect().top-scroller.getBoundingClientRect().top-150;
  }
  target.scrollIntoView({behavior:'instant',block:'start'});
  target.setAttribute('tabindex','-1');target.focus({preventScroll:true});
  $('status').textContent=moment?`Opened linked moment: ${moment.label}.`:`Opened case ${caseId}.`;
  if(caseMatch){showCase(caseId);linkedCaseDialog=true}
 });
}
function initializeEditorialLinks(){
 $('moment-links').innerHTML=DATA.moments.map(m=>`<li><a href="#${m.id}">${esc(m.label)}</a><button class="textbtn" data-copy-moment="${m.id}" aria-label="Copy link: ${esc(m.label)}">Copy link</button></li>`).join('');
 $('copy-case-link').onclick=()=>copyEditorialLink('case-'+selected,'case-link-feedback','case-link-fallback');
 document.addEventListener('click',e=>{const button=e.target.closest('[data-copy-moment]');if(button)copyEditorialLink(button.dataset.copyMoment,'moment-link-feedback','moment-link-fallback');const link=e.target.closest('a[href^="#"]');if(link&&link.getAttribute('href')===location.hash&&DATA.moments.some(m=>'#'+m.id===location.hash)){e.preventDefault();openEditorialMoment()}});
 for(const event of ['wheel','touchmove'])addEventListener(event,()=>{storyLinkPin=null},{passive:true});
 addEventListener('keydown',e=>{if(['ArrowDown','ArrowUp','PageDown','PageUp','Home','End',' '].includes(e.key))storyLinkPin=null});
 addEventListener('hashchange',openEditorialMoment);
 if(document.readyState==='complete')openEditorialMoment();else addEventListener('load',openEditorialMoment,{once:true});
}
initializeEditorialLinks();
