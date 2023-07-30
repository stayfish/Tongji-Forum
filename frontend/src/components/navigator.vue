<template>
    <el-menu :default-active="activeIndex" mode="horizontal" background-color="#ffffff" active-text-color="#5b21b6"
        @select="handleSelect" router>
        <el-menu-item :disabled="true">
            <span class="text-2xl text-dark" style="align-items: center;">
                Tongji
            </span>
        </el-menu-item>
        <div class="flex-grow2"></div>
        <el-menu-item index="/forum/index">
            论坛
        </el-menu-item>
        <el-menu-item index="/forum/dashboard">
            <div id="dashboard">
                管理
            </div>
        </el-menu-item>
        <el-menu-item :index="'/forum/homepage/' + store.state.user.username">
            用户
        </el-menu-item>
    </el-menu>
    <!-- <el-menu :default-active="activeIndex" router class="text-dark font-bold" mode="horizontal" background-color="#ffffff"
        active-text-color="#5b21b6" @select="handleSelect">
        <el-menu-item :disabled="true">
            <span class="text-2xl text-dark">Tongji</span>
        </el-menu-item>
        <el-menu-item index="/forum/index">
            论坛
        </el-menu-item>
        <el-menu-item v-if="isAdmin" index="/forum/dashboard">
            管理
        </el-menu-item>
        <el-menu-item :index="'/forum/homepage/' + store.state.user.username">
            用户
        </el-menu-item>
        <template>
            <div class="align-middle" style="align-items: center;">
                <User />
            </div>
        </template>
        <div class="flex-grow"></div>
    </el-menu> -->
    <el-backtop :right="100" :bottom="100" />
</template>

<script setup>
import Logout from '@/components/logout.vue'
import Search from '@/components/search.vue'
import User from '@/components/usericon.vue'
import { ref, reactive, computed } from 'vue'
import { useStore } from 'vuex'
const store = useStore()
const isAdmin = computed(() => {
    const level = Cookies.get('level')
    return level != 0
})
const defaultItem = '/forum/index'
let activeIndex = ref(defaultItem)

const handleSelect = (select) => {
    activeIndex = select
    console.log(activeIndex)
}

</script>
<style scoped>
.flex-grow {
    flex-grow: 1;
}

.flex-grow2 {
    flex-grow: 2;
}


.text-dark {
    color: #0D0C22
}
</style>