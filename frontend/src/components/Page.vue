<template>
    <div class="min-h-screen min-w-screen bg-gray-100 flex flex-col">
        <div class="no-expand" style="position: fixed; width: 100%">
            <Navigator></Navigator>
        </div>
        <div class="expand">
            <router-view></router-view>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import Navigator from '@/components/navigator.vue'
onMounted(() => {
    const fixdiv = document.querySelector('.no-expand')
    const content = document.querySelector('.expand')
    content.style.marginTop = fixdiv.offsetHeight + 'px'
    // content.style.height = window.innerHeight - fixdiv.offsetHeight + 'px'
})
</script>

<style scoped>
.no-expand {
    flex-grow: 0;
    z-index: 999;
}

.expand {
    flex-grow: 1;
    display: flex;
}
</style>