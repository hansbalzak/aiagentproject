package com.example.yourappname;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;

public class CalculatorActivity extends AppCompatActivity {

    private EditText editTextResult;
    private String currentInput = "";
    private String currentOperation = "";
    private double firstOperand = 0;
    private boolean isOperationSet = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calculator);

        editTextResult = findViewById(R.id.editTextResult);

        setButtonClickListener(R.id.buttonZero, "0");
        setButtonClickListener(R.id.buttonOne, "1");
        setButtonClickListener(R.id.buttonTwo, "2");
        setButtonClickListener(R.id.buttonThree, "3");
        setButtonClickListener(R.id.buttonFour, "4");
        setButtonClickListener(R.id.buttonFive, "5");
        setButtonClickListener(R.id.buttonSix, "6");
        setButtonClickListener(R.id.buttonSeven, "7");
        setButtonClickListener(R.id.buttonEight, "8");
        setButtonClickListener(R.id.buttonNine, "9");
        setButtonClickListener(R.id.buttonDot, ".");

        setOperationClickListener(R.id.buttonPlus, "+");
        setOperationClickListener(R.id.buttonMinus, "-");
        setOperationClickListener(R.id.buttonMultiply, "*");
        setOperationClickListener(R.id.buttonDivide, "/");

        findViewById(R.id.buttonClear).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clear();
            }
        });

        findViewById(R.id.buttonEquals).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                calculate();
            }
        });
    }

    private void setButtonClickListener(int id, String value) {
        Button button = findViewById(id);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                currentInput += value;
                editTextResult.setText(currentInput);
            }
        });
    }

    private void setOperationClickListener(int id, String operation) {
        Button button = findViewById(id);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (isOperationSet) {
                    calculate();
                }
                currentOperation = operation;
                firstOperand = Double.parseDouble(currentInput);
                currentInput = "";
                isOperationSet = true;
            }
        });
    }

    private void clear() {
        currentInput = "";
        currentOperation = "";
        firstOperand = 0;
        isOperationSet = false;
        editTextResult.setText("");
    }

    private void calculate() {
        if (currentInput.isEmpty() || !isOperationSet) {
            return;
        }
        double secondOperand = Double.parseDouble(currentInput);
        double result = 0;
        switch (currentOperation) {
            case "+":
                result = firstOperand + secondOperand;
                break;
            case "-":
                result = firstOperand - secondOperand;
                break;
            case "*":
                result = firstOperand * secondOperand;
                break;
            case "/":
                if (secondOperand != 0) {
                    result = firstOperand / secondOperand;
                } else {
                    editTextResult.setText("Error");
                    return;
                }
                break;
        }
        currentInput = String.valueOf(result);
        currentOperation = "";
        firstOperand = 0;
        isOperationSet = false;
        editTextResult.setText(currentInput);
    }
}
