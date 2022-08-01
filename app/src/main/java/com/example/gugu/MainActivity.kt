package com.example.gugu

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Gravity
import android.widget.*
import java.util.*

class MainActivity : AppCompatActivity() {
    lateinit var inputnum:EditText
    lateinit var button: Button
    lateinit var button2:Button
    lateinit var output_layout:LinearLayout
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        button=findViewById(R.id.button)
        button2=findViewById(R.id.button2)
        inputnum=findViewById(R.id.inputnum)
        output_layout=findViewById(R.id.output_layout)

        //입력 버튼을 누른 경우
        button.setOnClickListener{
            output_layout.removeAllViews() //구구단이 출력되는 뷰 내용을 지워줌
            if (inputnum.text.toString()!=""){ //입력된 내용이 있을 때
                val num:Int= Integer.parseInt(inputnum.text.toString())  //정수로 변환
                for(i in 1..9){ //곱하기1부터 9까지 FOR문을 통해 출력
                    val textView=TextView(this)
                    textView.gravity=Gravity.CENTER  //텍스트뷰를 중앙에 배치
                    textView.textSize=15F
                    textView.text= String.format("%d x %d =%d",num,(10-i),num * (10-i))//구구단을 TEXT로 전환
                    output_layout.addView(textView,0)//뷰에 추가
                }
                }else{
                Toast.makeText(this, "계산할 단을 입력하시오.", Toast.LENGTH_SHORT).show()
                //EDITTEXT에 값이 없을 경우 토스트 메시지 띄우기
            }
        }
        button2.setOnClickListener{
            output_layout.removeAllViews()
            inputnum.setText("")
            //INPUT과 뷰를 초기화
        }


    }
}



