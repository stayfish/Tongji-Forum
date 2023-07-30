<template>
    <el-row>
        <el-col :span="16">
            <el-descriptions column="1">
                <el-descriptions-item label="用户名" span='2'>{{ state.user.username }}</el-descriptions-item>
                <!-- <el-descriptions-item label="邮箱">{{ state.user.email }}</el-descriptions-item> -->
                <el-descriptions-item label="权限">
                    <el-tag>{{ levelName(state.user.level) }}</el-tag>
                </el-descriptions-item>
            </el-descriptions>
        </el-col>
        <el-col :span="8" class="text-center flex flex-col justify-between">
            <div v-if="show">
                <router-link :to="'/forum/homepage/' + props.username" class="text-base">用户主页</router-link>
            </div>
            <el-button @click="follow" :type="state.type" v-if="state.user.username != store.state.user.username">{{
                state.btnText
            }}</el-button>
        </el-col>
    </el-row>
</template>

<script setup>
import axios from '@/api'
import { reactive, ref } from 'vue';
import { useStore } from 'vuex'

const props = defineProps(['username', 'home'])
const show = ref(!props.home)
const state = reactive({
    user: '',
    type: '',
    btnText: ''
})
const btninfo = [
    { type: 'primary', btnText: '已关注' },
    { type: '', btnText: '关注' }
]
const username = props.username
const store = useStore()

const levelName = (level) => {
    if (level == 0)
        return '用户'
    else if (level == 1)
        return '管理员'
    else
        return '根管理员'
}

const getUser = async () => {
    try {
        const request = await axios.get(`/api/user/${username}`)
        if (request.status == 200) {
            // console.log(request.data)
            const user = request.data.users[0]
            state.user = user
            const index = user.followed ? 0 : 1;
            state.type = btninfo[index].type
            state.btnText = btninfo[index].btnText
        }
        else {
            console.log(request.status)
        }
    }
    catch (error) {
        console.log(error)
        console.log(request.status)
    }
}

const follow = async () => {
    const currentIndex = (state.type == 'primary') ? 0 : 1;
    try {
        let res = await axios.post(`/api/follow/${username}`)
        if (res.status == 200) {
            ElNotification({
                title: 'Success',
                message: '操作成功',
                type: 'success'
            })
            state.type = btninfo[1 - currentIndex].type
            state.btnText = btninfo[1 - currentIndex].btnText
        }

    }
    catch (error) {
        console.log(error)
    }
}

getUser()
</script>
