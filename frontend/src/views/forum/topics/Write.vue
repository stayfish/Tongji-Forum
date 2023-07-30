<template>
    <el-card>
        <el-button type="primary" @click="state.dialogVisible = true">发布</el-button>
        <el-dialog v-model="state.dialogVisible" title="发布" width="75%" :before-close="handleClose">
            <span class="font-bold">编辑标题</span>
            <el-input v-model="title"></el-input>
            <span class="font-bold">编辑内容</span>
            <v-md-editor v-model="text" height="400px"></v-md-editor>
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="state.dialogVisible = false">取消</el-button>
                    <el-button type="primary" @click="submitArticle">提交</el-button>
                </span>
            </template>
        </el-dialog>
    </el-card>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useStore } from 'vuex'
const title = ref('')
const text = ref('')
const state = reactive({
    dialogVisible: false,
})
const store = useStore()

async function submitArticle() {
    console.log(title.value)
    console.log(text.value)
    if (title.value.length == 0) {
        ElNotification({
            title: 'Warning',
            message: '标题不应为空',
            type: 'warning',
        })
    }
    else if (text.value.length == 0) {
        ElNotification({
            title: 'Warning',
            message: '内容不应为空',
            type: 'warning',
        })
    }
    else {
        state.dialogVisible = false
        data = {
            title: title.value,
            content: text.value,
            author: store.state.user.username
        }
        let res = await axios.post('/api/article/',)
    }
}
</script>