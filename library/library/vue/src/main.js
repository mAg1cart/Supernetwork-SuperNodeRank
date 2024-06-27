import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/assets/css/global.css'
import "element-ui/lib/theme-chalk/index.css";
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import '@/assets/icon/iconfont.js' // 图标
import '@/assets/icon/iconfont.css'
const app =createApp(App)
import * as ElIconModules from '@element-plus/icons'
import axios from "axios";
import request from "./utils/request";
for(let iconName in ElIconModules){
    app.component(iconName,ElIconModules[iconName])
}
app.use(store).use(router).use(ElementPlus,{locale: zhCn,size:"small"}).mount('#app')

request.interceptors.request.use(function (config) {
    config.headers['Authorization'] = localStorage.getItem('token')
    return config
})
