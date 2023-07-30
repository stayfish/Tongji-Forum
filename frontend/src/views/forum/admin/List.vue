<template>
    <el-table :data="state.table" 
    style="width: 100%">
        <el-table-column label="用户名" prop="username">
            <template #header>
                <IconField>
                    <template #icon><User class="icon" /></template>
                    <template #label>用户名</template>
                </IconField>
            </template>
            <template #default="scope">
                <span>{{ scope.row.username }}</span>
            </template>
        </el-table-column>
        <el-table-column label="邮箱" prop="email">
            <template #header>
                <IconField>
                    <template #icon><Message class="icon" /></template>
                    <template #label>邮箱</template>
                </IconField>
            </template>
        </el-table-column>
        <el-table-column label="权限" prop="level"
        :filters="[{ text: 'User', value: 0 }, { text: 'Admin', value: 1 }]"
        :filter-method="filterLevel"
        filter-placement="bottom-end"
        >
            <template #header>
                <IconField>
                    <template #icon><Management class="icon" /></template>
                    <template #label>权限</template>
                </IconField>
            </template>
            <template #default="scope">
                <el-tag>{{ levelName(scope.row.level) }}</el-tag>
            </template>
        </el-table-column>
        <el-table-column align="right">
            <template #header>
                <el-input v-model="search" placeholder="Search" 
                @input="searchKey(search)"
                />
            </template>
            <template #default="scope">
                <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
            </template>
        </el-table-column>
    </el-table>
</template>
<script setup>
// import Item from '@/views/admin/listItem.vue'
import { reactive, ref, computed, onMounted } from 'vue';
import {
    Message,
    User,
    InfoFilled,
    Management
} from '@element-plus/icons-vue'
import IconField from '@/components/iconfield.vue'
import axios from '@/api'
import { useStore } from 'vuex'

const store = useStore()
const step = 10
const search = ref('')

// const table = [
//     { useranme: 'ruoy', email: '1687559852@qq.com', level: 2 }
// ]
const state = reactive({
    table: [],
})
const AllUser = async () => {
    console.log(store.state.user['username'])
    let res = await axios.get('/api/user/')
    if (res.status == 200) {
        // table = res.data.users
        return res.data.users
    } else {
        console.log('用户数据请求失败')
        // table = None
        return None
    }
}

onMounted(async () => {
    console.log('mounted')
    state.table = await AllUser()
})

const levelName = (level) => {
    if (level == 0)
        return '用户'
    else if (level == 1)
        return '管理员'
    else 
        return '根管理员'
}

const filterLevel = (value, row) => {
    if (value == 0) 
        return row.level == 0
    else 
        return row.level !=0
}


const handleDelete = async (index, row) => {
    if (row.username == store.state.user['username']) {
        let res = await axios.delete(`/api/user/${row.username}`)
        if (res.status == 200) {
            state.table = await AllUser()
        } else {
            console.log('删除失败', res.status)
        }
    }
}

const searchKey = async (search) => {
    let res = await axios.get(`/api/user/${search}`)
    if (res.status == 200) {
        state.table = res.data.users
    } else {
        console.log('搜索失败', res.status)
        // table = None
        state.table = []
    }
}


// const filterTable = computed(() => {
//     table.filter((data) => data)
// })

</script>

<style scoped>
.list-container {
    border-style: solid;
    border-width: 4px;
}

.icon {
    width: 1.5em;
    height: 1.5em;
}
</style>