(window.webpackJsonp=window.webpackJsonp||[]).push([[30],{458:function(e,t,n){var content=n(465);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[e.i,content,""]]),content.locals&&(e.exports=content.locals);(0,n(30).default)("3a6f919c",content,!0,{sourceMap:!1})},464:function(e,t,n){"use strict";n(458)},465:function(e,t,n){var r=n(29)((function(i){return i[1]}));r.push([e.i,"span[data-v-5568ff5d]{color:#8acb88}.words[data-v-5568ff5d]{list-style-type:none;padding-left:0;overflow:hidden;font-size:1em}.cycler a[data-v-5568ff5d],.cycler a span[data-v-5568ff5d],.cycler span[data-v-5568ff5d]{text-align:left}.cycler a span[data-v-5568ff5d]{white-space:nowrap}.cycler[data-v-5568ff5d]{display:inline-block;position:relative;overflow:hidden}",""]),r.locals={},e.exports=r},470:function(e,t,n){"use strict";n.r(t);n(44),n(75);var r={name:"TextCycler",props:{items:{type:Object(Array),default:[["No items passed to text-cycler. The items prop was null or undefined",""]]},delay:{type:Number,default:2e3},stop:{type:Boolean,default:!1}},data:function(){var e=this;return setInterval((function(){e.currentIndex=++e.currentIndex%e.items.length}),e.delay),{currentIndex:0}},computed:{currentText:function(){return this.items[this.currentIndex]}}},c=(n(464),n(33)),component=Object(c.a)(r,(function(){var e=this,t=e._self._c;return t("div",{staticClass:"words cycler flex flex-center"},[""!==e.currentText[1]?t("a",{attrs:{href:"currentText[1]"}},[t("span",{domProps:{textContent:e._s(e.currentText[0])}})]):t("span",{domProps:{textContent:e._s(e.currentText[0])}}),e._v(" "),t("span",[e._v(".")])])}),[],!1,null,"5568ff5d",null);t.default=component.exports}}]);