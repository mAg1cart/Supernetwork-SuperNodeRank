<!-- 注册 -->
<template>
  <div style="height: 100vh; display: flex; align-items: center; justify-content: center;  background-color: beige;">
    <div style="display: flex; background-color: white; width: 50%; border-radius: 5px; overflow: hidden">
      <div style="flex: 1">
        <img src="@/assets/9.jpg" alt="" style="width: 100%">
      </div>
      <div style="flex: 1; display: flex; align-items: center; justify-content: center">
        <el-form :model="form" style="width: 80%" :rules="rules" ref="form">
          <div style="font-size: 20px; font-weight: bold; text-align: center; margin-bottom: 15px">用户注册</div>
          <el-form-item prop="username">
            <el-input prefix-icon="el-icon-user" size="medium" placeholder="请输入账号" v-model="form.username">
              <template #prefix>
                <el-icon class="el-input__icon"><User/></el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input prefix-icon="el-icon-lock" size="medium" show-password placeholder="请输入密码" v-model="form.password">
              <template #prefix>
                <el-icon class="el-input__icon"><Lock /></el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item prop="confirmPass">
            <el-input prefix-icon="el-icon-lock" size="medium" show-password placeholder="请确认密码" v-model="form.confirm">
              <template #prefix>
                <el-icon class="el-input__icon"><Lock /></el-icon>
              </template>
            </el-input>
          </el-form-item>
<!--          <el-form-item prop="role">-->
<!--            <el-radio v-model="form.role" label="2">读者</el-radio>-->
<!--            <el-radio v-model="form.role" label="1">管理员</el-radio>-->
<!--          </el-form-item>-->
          <el-form-item prop="role">
            <el-radio-group v-model="form.role">
              <el-radio label="2">读者</el-radio>
              <el-radio label="1">管理员</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item prop="authorize" v-if="form.role==1">
            <el-input v-model="form.authorize" placeholder="请输入管理员注册码" clearable show-password>
              <template #prefix>
                <el-icon class="el-input__icon"><Lock /></el-icon>
              </template>
            </el-input>
          </el-form-item>
          <el-form-item>
            <div style="display: flex">
              <el-input  v-model="form.validCode" style="width: 45%;" placeholder="请输入验证码">
                <template #prefix>
                  <el-icon class="el-input__icon"><Check /></el-icon>
                </template>
              </el-input>
              <ValidCode @input="createValidCode" style="width: 50%"/>
            </div>
          </el-form-item>
          <el-form-item>
            <el-button type="info" style="width: 100%" @click="register">注 册</el-button>
          </el-form-item>
          <div style="display: flex">
            <div style="flex: 1">已经有账号了？请 <span style="color: #6e77f2; cursor: pointer" @click="$router.push('/login')">登录</span></div>
          </div>
        </el-form>
      </div>
    </div>

  </div>

</template>

<script>
import request from "../utils/request";
import {ElMessage} from "element-plus";
import ValidCode from "../components/Validate";
import {Check} from "@element-plus/icons";
export default {
  name: "Login",
  components:{
    Check,
    ValidCode
  },
  data(){
    return{
      form:{},
      validCode: '',
      rules: {
        username: [
          {
            required: true,
            message: '请输入用户名',
            trigger: 'blur',
          },
          {
            min: 2,
            max: 13,
            message: '长度要求为2到13位',
            trigger: 'blur',
          },
        ],
        password: [
          {
            required: true,
            message: '请输入密码',
            trigger: 'blur',
          }
        ],
      confirm:[
        {
          required:true,
          message:"请确认密码",
          trigger:"blur"
        }
      ],
        authorize:[
          {
            required:true,
            message:"请输入注册码",
            trigger:"blur"
          }
        ],
      }
    }
    },

  methods:{
    createValidCode(data){
      this.validCode =data
    },
    register(){
      this.$refs['form'].validate((valid) => {
        if (valid) {
          if (!this.form.validCode) {
            ElMessage.error("请填写验证码")
            return
          }
          if(this.form.validCode.toLowerCase() !== this.validCode.toLowerCase()) {
            ElMessage.error("验证码错误")
            return
          }
          if(this.form.password != this.form.confirm)
          {
            ElMessage.error("两次密码输入不一致")
            return
          }
          if(this.form.role == 1 && this.form.authorize != "1234")
          {
            ElMessage.error("请输入正确的注册码")
            return
          }
          request.post("user/register",this.form).then(res=>{
            if(res.code == 0)
            {
              ElMessage.success("注册成功")
              this.$router.push("/login")
            }
            else {ElMessage.error(res.msg)}
          })
        }
      })

    }
  }

  }

</script>

<style scoped>

</style>