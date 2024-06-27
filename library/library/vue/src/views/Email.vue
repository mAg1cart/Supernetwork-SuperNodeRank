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
                    <div style="font-size: 20px; font-weight: bold; text-align: center; margin-bottom: 40px">
                        欢迎登录图书管理系统
                    </div>
                    <el-form-item>
                        <el-input v-model="form.email" size="medium" placeholder="请输入邮箱" clearable>
                            <template #prefix>
                                <el-icon class="el-input__icon">
                                    <User/>
                                </el-icon>
                            </template>
                        </el-input>

                    </el-form-item>

                    <el-form-item>
                        <el-input v-model="form.code" size="medium" placeholder="请输入邮箱验证码" clearable
                                  show-password>
                            <template #prefix>
                                <el-icon class="el-input__icon">
                                    <Lock/>
                                </el-icon>
                            </template>
                        </el-input>

                    </el-form-item>
                    <!--          <el-form-item >
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
                              </el-form-item>-->
                    <el-form-item>
                        <el-button type="primary" style="width: 100%" @click="send">发送验证码</el-button>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" style="width: 100%" @click="login">登 录</el-button>
                    </el-form-item>
                    <div style="display: flex">
                        <div style="flex: 1">还没有账号？请 <span style="color: #0f9876; cursor: pointer"
                                                                 @click="$router.push('/register')">注册</span></div>
                    </div>
                </el-form>
            </div>
        </div>


    </div>

</template>

<script>
import { setSkipLoginRedirect } from "@/utils/request";
import request from "../utils/request";
import {ElMessage} from "element-plus";
import ValidCode from "../components/Validate";

export default {
    name: "Login",
    components: {
        ValidCode
    },
    data() {
        return {
            // validCode: '',//通过valicode获取的验证码
            form: {
                email: "",
                code: ""
            },

        }

    },
    methods: {

        /*createValidCode(data) {
            this.validCode = data
        },*/
        send() {//发送验证码
            setSkipLoginRedirect(true);// 设置标志变量
            var email = this.form.email;
            const encodedEmail = encodeURIComponent(email);
            console.log(email);

            request.post('/user/sendCode',{email:email}).then(res => {
                if (res.code == 200) {
                    ElMessage.success(res.msg);
                } else {
                    ElMessage.error(res.msg)
                }
            }).finally(() => {
                setSkipLoginRedirect(false); // 重置标志变量
            })
        },
        login() {//判断验证码
            var email = this.form.email;
            var code = this.form.code;

            request.post('/user/loginByCode', {
                email: email,
                code: code
            }).then(response => {
                if (response.code == "200") {
                    console.log("Login successful:", response.data);
                    sessionStorage.setItem("user",JSON.stringify(response.data))//缓存用户信息
                    this.$router.push("/dashboard")
                    ElMessage.success("登录成功")
                } else {
                    console.error("Error:", response.data.message);
                }
            }).catch(error => {
                console.error("Request failed:", error);
            });
        }
    }
}

</script>

<style scoped>
.login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
//background: #2186dc; background-image: url("../assets/img/bg2.dd39329b.svg") !important;

    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}
</style>