<template>
    <el-row class="flex-row justify-between expand">
        <el-col :sm="6" style="position: relative;" id="sidebar">
            <div style="position: fixed; height: 100vh; width: 25vw">
                <Topics></Topics>
            </div>
        </el-col>
        <el-col :sm="12">
            <router-view></router-view>
            <!-- <Display></Display> -->
        </el-col>
        <el-col :sm="6">
            <div class="fixed-pos">
                <Hot></Hot>
                <Edit></Edit>
                <el-card>
                    <Logout />
                </el-card>
            </div>
        </el-col>
    </el-row>
</template>
<script setup>
import Topics from './Topics.vue'
import Logout from '@/components/logout.vue'
import Hot from './hot.vue'
import Edit from './Edit.vue'
import { onMounted } from 'vue';
onMounted(() => {
    const sidebar = document.getElementById('sidebar')
    const topics = sidebar.querySelector('div')
    topics.style.width = sidebar.offsetWidth

})
</script>

<style scoped>
.expand {
    flex-grow: 1;
    display: flex;
}

.fixed-pos {
    position: fixed;
    width: 25vw;
    top: 15vh
}
</style>
