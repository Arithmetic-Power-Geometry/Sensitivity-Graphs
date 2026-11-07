// P02 independent JavaScript checker: no dependencies, no Python/SymPy.
// Reconstruct graph from 5-bit truth tables; BFS components; 5x5 Gram polynomial
// via Faddeev-LeVerrier exact integer recurrence.
const cases={A:["00000","01000","10000","11100","11111"],B:["00000","00011","00101","01000","10000"]};
function verify(bits){
 const S=new Set(bits.map(s=>parseInt(s,2))), adj=Array.from({length:32},()=>[]);let edges=0;
 for(let x=0;x<32;x++)for(let k=0;k<5;k++){const y=x^(1<<k);
  if(x<y && S.has(x)!==S.has(y)){adj[x].push(y);adj[y].push(x);edges++}}
 const components=[],visited=new Set();
 for(let x=0;x<32;x++){if(!adj[x].length||visited.has(x))continue;
  const q=[x];visited.add(x);
  for(let i=0;i<q.length;i++)for(const y of adj[q[i]])if(!visited.has(y)){visited.add(y);q.push(y)}
  let diam=0;
  for(const root of q){const dist=new Map([[root,0]]),queue=[root];
   for(let j=0;j<queue.length;j++)for(const y of adj[queue[j]])if(!dist.has(y)){
    dist.set(y,dist.get(queue[j])+1);queue.push(y)}
   diam=Math.max(diam,...dist.values())}
  components.push([q.length,diam])}
 const positive=[...S].sort((a,b)=>a-b);
 const gram=positive.map(x=>positive.map(y=>adj[x].filter(z=>adj[y].includes(z)).length));
 let B=Array.from({length:5},(_,i)=>Array.from({length:5},(_,j)=>+(i===j))),coef=[];
 for(let k=1;k<=5;k++){
  const P=gram.map((row,i)=>row.map((_,j)=>row.reduce((s,v,l)=>s+v*B[l][j],0)));
  const tr=P.reduce((s,row,i)=>s+row[i],0),c=-tr/k;coef.push(c);
  B=P.map((row,i)=>row.map((v,j)=>v+(i===j?c:0)))}
 return {edges,isolates:adj.filter(x=>!x.length).length,components:components.sort((a,b)=>b[0]-a[0]),
  gram,characteristicCoefficients:[1,...coef]};
}
const a=verify(cases.A),b=verify(cases.B);
const eq=(x,y)=>JSON.stringify(x)===JSON.stringify(y);
if(!eq(a.characteristicCoefficients,[1,-21,162,-578,957,-585])||
 !eq(a.characteristicCoefficients,b.characteristicCoefficients)||
 !eq(a.components,[[16,6],[4,2]])||!eq(b.components,[[11,4],[9,4]])||
 a.edges!==21||b.edges!==21||a.isolates!==12||b.isolates!==12)throw Error("FAIL");
console.log(JSON.stringify({A:a,B:b,pass:true},null,2));
