<template>
    <el-main justify="center">
      <el-result
        icon="error"
        title="404 Not Found"
        sub-title="页面走丢了"
      >
        <template #extra>
          <el-button type="primary" @click="$router.push('/login')">回到主页</el-button>
        </template>
      </el-result>
    </el-main>
</template>