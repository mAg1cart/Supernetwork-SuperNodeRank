
<template>
  <div class="talkContent">
    <div class="talkShow">
      <div :class="[(item.person=='mechanical')?'mechanicalTalk':'mineTalk']" v-for="(item,index) in talkList" :key="index">
        <span>{{item.say}}</span>
      </div>
    </div>
    <div class="talkInput">
      <form @submit.prevent="getQuestion" class="userSearch">
        <el-input
            placeholder="请输入内容"
            v-model="contentVal"
            size="big">
          <i slot="suffix" class="el-input__icon el-icon-position" style="cursor: pointer;" @click="getQuestion"></i>
        </el-input>
      </form>
    </div>
  </div>
</template>

<script>
import request from "../utils/request";
import {ElMessage} from "element-plus";

export default {

  data() {
    return {
      talkList: [
        { id:"1", person: 'mechanical', say: '你好，我是图书馆AI小助手^_^,请问有什么可以帮到你呢？' },
      ],
      isMine: 1,
      contentVal: '',
    };
  },
  methods: {
    getQuestion() {
      if (this.contentVal == '') {
        this.$message.error('请输入内容');
        return;
      }

      // admin提问数据push()
      this.talkList.push({ id: Date.now(), person:'admin', say: this.contentVal });
      // 清空输入栏数据
      let question=this.contentVal
      this.contentVal = '';
      this.getAnswer(question);
    },
    async getAnswer(question){
      // 调用API获取回答， 模拟后端返回的数据流式输出
      let data ='';

      // mechanical 模拟回答
      request.get(`/chat?question=${question}`).then((res) => {
   ;
        if(res.code==200){
          data = ''+res.msg;
          this.talkList.push({ id: Date.now(), person:'mechanical', say: '...' });
          // 流式输出文字逐个展示
          let text = "";
          const length = this.talkList.length;
          for (let i = 0; i < data.length; i++) {
            text += data.charAt(i);
             new Promise((resolve) => {
              setTimeout(resolve, 100)
            });
            this.talkList[length - 1].say= text;
          }
        }else{
          ElMessage.error(res.msg);
        }
      })


    }
  },
};
</script>

<style scoped>
.talkContent {
  margin: 50px auto 0;
  font-size: 14px;
}

.talkShow {
  height: 400px;
  margin: 10px auto 0;
  overflow: auto;
}

.talkInput {
  margin: 10px auto 0;
  display:flex;
  justify-content: left;
  width: 200%;
  border-color: white;
  border-radius: 0;

}

.mechanicalTalk {
  margin: 10px;
}

.mechanicalTalk span {
  display: inline-block;
  background: white;
  border-radius: 10px;
  padding: 5px 10px;
  border: 1px solid rgb(214, 216, 219);
  border-top-left-radius: 0px;
  word-break: break-all;
  text-align: left;
}

.mineTalk {
  margin: 10px;
  text-align: right;
}

.mineTalk span {
  display: inline-block;
  border-radius: 10px;
  border-top-right-radius: 0px;
  background: #409eff;
  color: #fff;
  padding: 5px 10px;
  word-break: break-all;
  text-align: left;
}

</style>

