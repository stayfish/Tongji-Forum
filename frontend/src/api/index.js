import axios from 'axios'
import Cookies from 'js-cookie'


// axios.defaults.baseURL = 'http://127.0.0.1:5000/';
// axios.defaults.baseURL = 'http://127.0.0.1:3246/';
axios.defaults.baseURL = '';


// 请求拦截器
axios.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    if (config.url !== '/api/login/') {
    // if (config.url !== 'api/login/') {
      const token = Cookies.get('token')
      if(token) {
        config.headers['token'] = token
      }
    }
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });

// 添加响应拦截器
axios.interceptors.response.use(function (response) {
    // 2xx 范围内的状态码都会触发该函数。
    // 对响应数据做点什么
    console.log('response ok')
    // return Promise.resolve(response)
    return response;
  }, function (error) {
    // 超出 2xx 范围的状态码都会触发该函数。
    // 对响应错误做点什么
    console.log('response fail')
    console.log(response)
    return Promise.reject(error);
  });

export default axios