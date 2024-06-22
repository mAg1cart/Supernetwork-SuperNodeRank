<template>
<!-- <div style="height: 50px; line-height:50px; border-bottom: 1px solid #ccc; display: flex">-->
<!--   <div style="width: 200px; padding-left:30px; font-weight: bold; color:dodgerblue">-->
<!--     <img :src="imgUrl" class="icon" >-->
<!--     图书管理系统</div>-->
<!--   <div style="flex: 1"></div>-->
<!--   <div style="width: 100px">-->
<!--     <el-dropdown>-->
<!--      <span class="el-dropdown-link">-->
<!--        {{user.nickName}} <el-icon class="el-icon&#45;&#45;right">-->
<!--          <arrow-down />-->
<!--          </el-icon>-->
<!--      </span>-->
<!--       <template #dropdown>-->
<!--         <el-dropdown-menu>-->
<!--           <el-dropdown-item @click="exit">退出系统</el-dropdown-item>-->
<!--         </el-dropdown-menu>-->
<!--       </template>-->
<!--     </el-dropdown>-->
<!--  -->
<!--   </div>-->
<!-- </div>-->
  <!-- 头部 -->
  <el-header>
    <div class="head-bar">
      <div class="header-ico">
        <!--      <i class="el-icon-s-home"></i>-->
        <img src="@/assets/img/1.png" style="width: 71px;
    height: 55px;
    margin-left: -25px;
    margin-top: 5px;">
      </div>
      <div class="logo">图书管理系统</div>
      <div class="head-right">
        <div class="head-user-con">


          <div class="user-avatar">
            <img src="../assets/11.jpg" />
          </div>

          <el-dropdown @command="handleCommand" class="user-name" trigger="click">
          <span class="el-dropdown-link">
           <span>欢迎您，<b>
             <span class="name" v-if="user.role==1"> 管理员：</span>
          <span class="name" v-if="user.role==2"> 读者：</span>
        </b>&nbsp;&nbsp;{{user.username}}</span>
            <i class="el-icon-caret-bottom"></i>
          </span>
            <template #dropdown>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item command="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
            </template>
          </el-dropdown>


        </div>
      </div>
    </div>

  </el-header>




</template>

<script>
import {ElMessage} from "element-plus";

export default {
  name: "Header",
  props: ['user'],
  data(){
    return{
      user:[],
      imgUrl:require("../assets/icon/login.png")
    }
  },
  created(){
    let userStr = sessionStorage.getItem("user")||"{}"
    this.user = JSON.parse(userStr)
  },
  methods:{
    exit(){
      sessionStorage.removeItem("user")
      this.$router.push("/login")
      ElMessage.success("退出系统成功")
    },
    handleCommand(command) {
      if (command === "logout") {
        this.$confirm("此操作将退出登录, 是否继续?", "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        })
            .then(() => {
              sessionStorage.removeItem("user")
              this.$message({
                type: "success",
                message: "退出登录成功!",
              });
              this.$router.push("login");
            })
            .catch(() => {
              this.$message({
                type: "info",
                message: "已取消",
              });
            });

      }
    },
  }

}
</script>

<style scoped>
.icon {
  width: 40px;
  height: 40px;
  padding-top: 5px;
  padding-right: 10px;
}
.title{
  cursor: pointer;
}
.el-header {
  background-color: #427cb3;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.words {
  text-align: center;
}
span {
  color: black;
}
.el-container{
  height: 100%;
}
.el-aside{
  background-color:#353744;
  border-right: 1px solid lightgrey;
}
.el-menu{
  border: 0;
}
.head-bar {
  position: relative;
  box-sizing: border-box;
  width: 100%;
  height: 70px;
  font-size: 18px;
  color: #fff;

}

.header-ico {
  float: left;
  padding: 0 21px;
  line-height: 70px;
}

.head-bar .logo {
  float: left;
  width: 250px;
  line-height: 70px;
  margin-left: -25px;
}

.head-right {
  float: right;
  padding-right: 50px;
}

.head-user-con {
  display: flex;
  height: 70px;
  align-items: center;
}

.btn-fullscreen {
  transform: rotate(45deg);
  margin-right: 5px;
  font-size: 24px;
}

.btn-fullscreen {
  position: relative;
  width: 30px;
  height: 30px;
  text-align: center;
  border-radius: 15px;
  cursor: pointer;
}

.btn-bell .el-icon-bell {
  color: #fff;
}

.user-name {
  margin-left: 10px;
}

.user-avatar {
  margin-left: 20px;
}

.user-avatar img {
  display: block;
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.el-dropdown-link {
  color: #fff;
  cursor: pointer;
}

.el-dropdown-menu__item {
  text-align: center;
}
</style>