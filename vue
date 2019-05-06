1、首先axios不支持vue.use()方式声明使用，看了所有近乎相同的axios文档都没有提到这一点 
建议方式

在main.js中如下声明使用
import axios from 'axios';
Vue.prototype.$axios=axios;
那么在其他vue组件中就可以this.$axios调用使用
--------------------- 
作者：BeterJane 
来源：CSDN 
原文：https://blog.csdn.net/u012369271/article/details/72848102 
版权声明：本文为博主原创文章，转载请附上博文链接！
