import axios from "axios";
import { createRouter, createWebHashHistory } from "vue-router";
import store from '@/store'
import { compile } from "vue";
const routes = [
    {
        path: '/',
        redirect: { name: 'Login' },
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/login/Login.vue')
    },
    {
        path: '/signup',
        name: 'Signup',
        component: () => import('@/views/signup/Signup.vue')
    },
    {
        path: '/forum',
        name: 'Forum',
        component: () => import('@/components/Page.vue'),
        redirect: '/forum/index',
        children: [
            {
                path: 'dashboard',
                name: 'Dashboard',
                component: () => import('@/views/forum/admin/Dashboard.vue')
            },
            {
                path: 'homepage/:username',
                name: 'Home',
                component: () => import('@/views/forum/profile/HomePage.vue')
            },
            {
                path: 'index',
                name: 'Index',
                component: () => import('@/views/forum/topics/Index.vue'),
                redirect: { name: 'Display' },
                children: [
                    {
                        path: 'display',
                        name: 'Display',
                        component: () => import('@/views/forum/topics/Display.vue'),
                    },
                    {
                        path: 'article/:id',
                        name: 'Article',
                        component: () => import('@/views/forum/topics/Article.vue')
                    }
                ]
            },
            // {
            //     path: 'profile/:username',
            //     name: 'Profile',
            //     component: () => import('@/views/forum/profile/Profile.vue')
            // },

        ]
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: () => import('@/views/404.vue')
    },

]
const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})

router.beforeEach((to, from) => {
    console.log(to, from)
    console.log(router)
    const token = Cookies.get('token')
    // 登陆验证
    if (!token && to.path !== '/login' && to.path !== '/signup') {
        ElNotification({
            title: 'Failure',
            message: '请先登录',
            type: 'error'
        })
        return { name: 'Login' }
    }
    let data = Cookies.get('username')
    store.commit('set_userinfo', {
        username: data,
    })
    // 防止重复登陆
    if (token && to.path === '/login') {
        return { name: 'Forum' }
    }
    const level = Cookies.get('level')
    if (level == 0 && to.path === '/forum/dashboard') {
        ElNotification({
            title: 'Failure',
            message: '权限不足',
            type: 'error'
        })
        return { name: 'Forum' }
    }
    return true
})

export default router