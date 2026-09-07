const moduleCopy={
  llm:'Explain an LLM in plain language, choose useful first tasks, and check important output.',
  prompt:'Direct AI toward a useful outcome, test the result, and improve the interaction.',
  context:'Planned: assemble and maintain the information AI needs for a task.',
  harness:'Planned: understand goal-seeking AI and configure the tools, rules, memory, files, and interfaces around a model.',
  loop:'Planned: build measured feedback cycles that improve repeatable AI work.'
};
const moduleDetail=document.querySelector('#moduleDetail');
const moduleButtons=[...document.querySelectorAll('.module')];
function selectModule(button){moduleButtons.forEach(b=>b.classList.toggle('active',b===button));moduleDetail.textContent=moduleCopy[button.dataset.module]}
moduleButtons.forEach(button=>button.addEventListener('click',()=>selectModule(button)));
selectModule(moduleButtons[0]);

const tabs={
  lesson:`<div class="content-grid"><article class="content-card"><span class="num">01 · INVITE</span><h3>Start with their words</h3><p>“How would you explain an LLM to a coworker?” A rough answer is completely fine—and it is never graded.</p></article><article class="content-card"><span class="num">02 · TEACH</span><h3>Pattern-based predictor</h3><p>Connect the idea to familiar autocomplete, then explain where that comparison stops being accurate.</p></article><article class="content-card"><span class="num">03 · APPLY</span><h3>Make it useful at work</h3><p>Draft from approved source material, then check facts, missing details, meaning, and impact.</p></article></div>`,
  check:`<div class="question-card"><p class="eyebrow">Sample formative check · no letter grade</p><h3>A polished summary names an unfamiliar action owner. What is the best response?</h3><div class="answer-list"><button class="answer weak">A. Assume it found newer information online.</button><button class="answer strong">B. Compare the response with the notes and correct the detail.</button><button class="answer weak">C. Ask the AI if it is sure.</button><button class="answer best">D. Tell it not to guess unsupported details and still compare the next response with the notes.</button></div><div class="feedback" hidden></div></div>`,
  evidence:`<div class="evidence-grid"><article class="evidence-card"><b>1 · Contained exercise</b><h3>Explain it plainly</h3><p>Correct a coworker's “search engine that knows everything” description in two or three sentences.</p></article><article class="evidence-card"><b>2 · Workplace application</b><h3>Choose a useful task</h3><p>Name what to provide, what response to request, and what to check before using it.</p></article><article class="evidence-card"><b>3 · Reusable artifact</b><h3>LLM Working Card</h3><p>Capture an explanation, analogy, appropriate tasks, needed information, and a verification habit.</p></article></div>`,
  media:`<div class="media-list"><a class="media-card" href="https://www.youtube.com/watch?v=5sLYAQS9sWQ" target="_blank" rel="noreferrer"><span>Short video · IBM Technology</span><strong>How Large Language Models Work ↗</strong><small>Offer after the in-chat explanation for a compact visual mental model.</small></a><a class="media-card" href="https://podcasts.apple.com/us/podcast/what-are-large-language-models/id1613112649?i=1000633663969" target="_blank" rel="noreferrer"><span>Six-minute audio · Cognixia</span><strong>What Are Large Language Models? ↗</strong><small>An optional audio explanation for learners who prefer to listen.</small></a><a class="media-card" href="https://developers.google.com/machine-learning/crash-course/llm" target="_blank" rel="noreferrer"><span>Deeper reading · Google</span><strong>Introduction to LLMs ↗</strong><small>A more technical path, offered only when a learner wants to go deeper.</small></a></div>`
};
const tabButtons=[...document.querySelectorAll('[role=tab]')];
const panel=document.querySelector('#tabPanel');
function activateTab(name){tabButtons.forEach(b=>b.setAttribute('aria-selected',String(b.dataset.tab===name)));panel.innerHTML=tabs[name];if(name==='check')wireAnswers()}
function wireAnswers(){const feedback=panel.querySelector('.feedback');panel.querySelectorAll('.answer').forEach(answer=>answer.addEventListener('click',()=>{panel.querySelectorAll('.answer').forEach(a=>a.classList.add('revealed'));feedback.hidden=false;if(answer.classList.contains('best'))feedback.innerHTML='<strong>Best choice.</strong> It improves the instruction and still verifies the result against the source.';else if(answer.classList.contains('strong'))feedback.innerHTML='<strong>A strong response.</strong> It catches the current error. D goes one step further by reducing the chance of another unsupported detail while still checking the source.';else feedback.innerHTML='<strong>There is a better safeguard.</strong> Fluent output can sound certain even when a detail is unsupported. Improve the instruction and compare the result with the approved notes.'}))}
tabButtons.forEach(button=>button.addEventListener('click',()=>activateTab(button.dataset.tab)));
activateTab('lesson');

const dialog=document.querySelector('#explainerDialog');
document.querySelector('#openExplainer').addEventListener('click',()=>dialog.showModal());
dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close()});
