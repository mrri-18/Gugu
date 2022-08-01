package com.example.gugu

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler

class SplashActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        //DURATION 시간동안 대표화면 실행
        Handler().postDelayed({
            val intent = Intent(this, MainActivity::class.java)
            intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION)
            startActivity(intent)
            finish()
        },DURATION)

    }
    //지속시간 설정
    companion object {
        private const val DURATION : Long = 3000
    }
    //뒤로가기 설정
    override fun onBackPressed() {
        super.onBackPressed()
    }
}