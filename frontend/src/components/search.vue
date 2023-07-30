<template>
    <div class="flex">
        <el-input v-model="search" placeholder="Search" style="align-items: center;" @input="searchKey(search)">
            <template #suffix>
                <el-button :icon="Search" text />
            </template>
        </el-input>
    </div>
</template>

<script setup>
import { Search } from '@element-plus/icons-vue'
import { ref } from 'vue'
const search = ref('')
</script>