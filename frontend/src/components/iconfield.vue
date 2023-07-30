<template>
    <el-row>
        <el-col :sm='4' :xs="0" class="icon">
            <slot name="icon"></slot>
        </el-col>
        <el-col :sm="20" :xs="24">
            <el-text>
                <slot name="label"></slot>
            </el-text>
        </el-col>
    </el-row>
</template>
