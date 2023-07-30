<template>
    <el-row>
        <el-col :sm="4"></el-col>
        <el-col :xs="24" :sm="16">
            <div style="width: 100%" class="mt-8 flex flex-col align-middle">
                <div class="flex">
                    <el-input v-model="input" @input="search" placeholder="Search" style="align-items: center;">
                        <template #suffix>
                            <el-icon>
                                <Search />
                            </el-icon>
                        </template>
                    </el-input>
                </div>
                <el-empty v-if="state.articles.length == 0" description="没有文章~" />
                <div v-for="article in state.articles" :key="article.id">
                    <!-- <Articles :article="article"></Articles> -->
                    <Preview :article="article"></Preview>
                </div>
            </div>
        </el-col>
    </el-row>
</template>

<script setup>

import Preview from './Preview.vue'
import { reactive, ref } from 'vue';
import { Search } from '@element-plus/icons-vue'
import axios from '@/api'
const input = ref('')
const state = reactive({
    articles: '',
})

async function search() {
    if (input.value.length == 0) {
        AllArticles()
    }
    try {
        let res = await axios.get(`/api/article/search/${input.value}`)
        if (res.status == 200) {
            state.articles = res.data.articles
        } else {
            console.log(res.status)
        }
    }
    catch (error) {
        console.log(error)
    }
}

const AllArticles = async () => {
    try {
        let res = await axios.get('/api/article/')
        // console.log("all-articles", res)
        state.articles = res.data.articles
    }
    catch (error) {
        console.log(`AllArticles: ${error}`)
    }
}

AllArticles()
</script>