import { createApp } from 'vue'
// import './style.css'
import App from './App.vue'
import router from '@/router'
import 'virtual:windi.css'
import store from '@/store'

import VMdEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
import VueMarkdownEditor from '@kangc/v-md-editor';
import createKatexPlugin from '@kangc/v-md-editor/lib/plugins/katex/cdn';

// highlightjs
import hljs from 'highlight.js';

const app = createApp(App)
VMdEditor.use(githubTheme, {
  Hljs: hljs,
});
VMdPreview.use(githubTheme, {
  Hljs: hljs,
});
VueMarkdownEditor.use(createKatexPlugin());
VMdPreview.use(createKatexPlugin())
app.use(VMdPreview);
app.use(VMdEditor)

app.use(store)
app.use(router)
app.mount('#app')

