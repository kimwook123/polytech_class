package test20;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/guguTest2")
public class GuguTest2Servlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 1. 한글 인코딩 설정
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html; charset=utf-8");

        PrintWriter out = response.getWriter();
        
        // 2. 파라미터 가져오기 (단수)
        String danStr = request.getParameter("dan");

        out.print("<html><head><title>구구단 출력</title></head><body>");

        if (danStr != null && !danStr.isEmpty()) {
            try {
                int dan = Integer.parseInt(danStr);
                
                // 테이블 시작 및 스타일 지정
                out.print("<table border='1' width='800' align='center'>");
                
                // 테이블 헤더 (노란색 배경, 2칸 병합)
                out.print("<tr bgcolor='#FFFF66'>");
                out.print("<td colspan='2' align='center'><b>" + dan + " 단 출력</b></td>");
                out.print("</tr>");
                
                // 구구단 계산 및 행 배경색 교대 출력
                for (int i = 1; i <= 9; i++) {
                    // i가 홀수인지 짝수인지 판별하여 배경색 변경
                    if (i % 2 == 1) { 
                        // 홀수 행: 파란색 계열
                        out.print("<tr bgcolor='#99CCFF'>");
                    } else {
                        // 짝수 행: 연두색 계열
                        out.print("<tr bgcolor='#CCFFCC'>");
                    }
                    
                    // 각 열(td)에 수식과 결과 출력
                    out.print("<td align='center'>" + dan + " * " + i + "</td>");
                    out.print("<td align='center'>" + (dan * i) + "</td>");
                    out.print("</tr>");
                }
                
                out.print("</table>");
                
            } catch (NumberFormatException e) {
                out.print("<h3 align='center'>올바른 숫자를 입력해주세요.</h3>");
            }
        }else {
            // 이 부분이 화면에 단수 입력창(Form)을 만들어주는 코드입니다!
            out.print("<h3 align='center'>구구단 출력기</h3>");
            out.print("<div align='center'>");
            out.print("<form method='get' action='guguTest2'>");
            out.print("출력할 단수 : <input type='number' name='dan' min='2' max='9' required> ");
            out.print("<input type='submit' value='출력'>");
            out.print("</form>");
            out.print("</div>");
        }

        out.print("</body></html>");
    }
}