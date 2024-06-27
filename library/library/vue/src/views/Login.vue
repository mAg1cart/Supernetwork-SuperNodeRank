<template>
  <div
      style="height: 100vh;
  display: flex; align-items: center;
  justify-content: center;

  "
      class="login-wrap"
>
    <div style="display: flex; background-color: white; width: 30%;height: 50%; border-radius: 5px; overflow: hidden">
      <div style="flex: 1; display: flex; align-items: center; justify-content: center">
        <el-form :model="form" style="width: 80%" :rules="rules" ref="form">
          <div style="font-size: 20px; font-weight: bold; text-align: center; margin-bottom: 40px">欢迎登录图书管理系统</div>
          <el-form-item prop="username">
                    <el-input v-model="form.username" size="medium" placeholder="请输入账号"  clearable>
                    <template #prefix>
                       <el-icon class="el-input__icon"><User /></el-icon>
                    </template>
                   </el-input>

          </el-form-item>

          <el-form-item prop="password">
            <el-input v-model="form.password"   size="medium"  placeholder="请输入密码" clearable show-password>
              <template #prefix>
                <el-icon class="el-input__icon" ><Lock /></el-icon>
              </template>
            </el-input>

          </el-form-item>
          <el-form-item prop="code">
            <div style="display: flex">
              <el-input placeholder="请输入验证码" prefix-icon="el-icon-circle-check" size="medium" style="flex: 1" v-model="form.validCode">
                <template #prefix>
                  <el-icon class="el-input__icon" ><Check/></el-icon>
                </template>
              </el-input>
              <div style="flex: 1; height: 36px;margin-left: 13px">

                <ValidCode @input="createValidCode" style="width: 50%"/>
              </div>
            </div>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" style="width: 100%" @click="login">登 录</el-button>
          </el-form-item>
          <div style="display: flex">
              <div style="flex: 1">还没有账号？请 <span style="color: #0f9876; cursor: pointer" @click="$router.push('/register')">注册</span></div>
              <div style="flex: 1"><span style="color: #0f9876; cursor: pointer" @click="$router.push('/email')">邮箱登录</span></div>
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

export default {
  name: "Login",
  components:{
    ValidCode
  },
  data() {
    return {
      validCode: '',//通过valicode获取的验证码
      form: {},
      rules: {
        username: [
          {
            required: true,
            message: '请输入用户名',
            trigger: 'blur',
          }
        ],
        password: [
          {
            required: true,
            message: '请输入密码',
            trigger: 'blur',
          }
        ]

      }

    }
  },
  methods: {
    createValidCode(data){
      this.validCode = data
    },
    login(){
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

          request.post("user/login", this.form).then(res => {
            if (res.code == 200) {
              //ElMessage.success("哈哈:"+res.data)
              const token=res.data.token
              localStorage.setItem("token", token)
              //ElMessage.success(token)
              sessionStorage.setItem("user",JSON.stringify(res.data))//缓存用户信息
              this.$router.push("/dashboard")
            } else {
              ElMessage.error(res.msg)
            }
          })
        }
      })

    }
  }
}

</script>

<style scoped>
.login-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  //background: #2186dc;
  background-image: url("../assets/img/bg2.dd39329b.svg")!important;

  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
</style>