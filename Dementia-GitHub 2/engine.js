/* Pure presentation state: independent of rendering and animation timing. */
(function(root){
class DeckState {
 constructor(counts,index=0,build=0){if(!Array.isArray(counts)||!counts.length||counts.some(n=>!Number.isInteger(n)||n<1))throw new Error('Invalid build counts');this.counts=counts;this.index=0;this.build=0;this.jump(index,build)}
 jump(index,build=0){this.index=Math.max(0,Math.min(this.counts.length-1,Number.isFinite(index)?Math.trunc(index):0));this.build=Math.max(0,Math.min(this.counts[this.index]-1,Number.isFinite(build)?Math.trunc(build):0));return this.snapshot()}
 advance(){if(this.build<this.counts[this.index]-1)this.build++;else if(this.index<this.counts.length-1){this.index++;this.build=0}return this.snapshot()}
 back(){if(this.build>0)this.build--;else if(this.index>0){this.index--;this.build=this.counts[this.index]-1}return this.snapshot()}
 snapshot(){return {index:this.index,build:this.build}}
 get progress(){const total=this.counts.reduce((a,b)=>a+b,0)-1;const before=this.counts.slice(0,this.index).reduce((a,b)=>a+b,0);return total?(before+this.build)/total:1}
}
if(typeof module!=='undefined'&&module.exports)module.exports={DeckState};else root.DeckState=DeckState;
})(typeof window!=='undefined'?window:globalThis);
