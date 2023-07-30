<template>
    <el-row class="flex-row justify-between expand">
        <el-col :sm="6" style="position: relative;" id="sidebar">
            <div style="position: fixed; height: 100vh; width: 25vw">
                <Options></Options>
            </div>
        </el-col>
        <el-col :sm="18">
            <List></List>
        </el-col>
    </el-row>
</template>

<script setup>
import List from './List.vue'
import Options from './Options.vue'

</script>