package test20;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/gugudan")
public class GugudanServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 1. 한글 깨짐 방지를 위한 인코딩 설정
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html; charset=utf-8");

        PrintWriter out = response.getWriter();
        
        // 2. 'dan' 파라미터 값 가져오기
        String danStr = request.getParameter("dan");

        out.print("<html><head><title>구구단 출력기</title></head><body>");

        // 3. 파라미터가 없으면(최초 접속 시) 입력 폼 출력
        if (danStr == null || danStr.isEmpty()) {
            out.print("<h2>구구단 출력기</h2>");
            out.print("<form method='get' action='gugudan'>");
            out.print("출력할 단수 입력 : <input type='number' name='dan' min='2' max='9' required> 단 ");
            out.print("<input type='submit' value='출력'>");
            out.print("</form>");
        } 
        // 4. 파라미터가 전달되면(단수 입력 시) 구구단 계산 및 출력
        else {
            try {
                // 문자열로 전달된 파라미터를 정수로 변환
                int dan = Integer.parseInt(danStr);
                
                out.print("<h2>" + dan + "단 출력 결과</h2>");
                out.print("<table border='1' cellpadding='5' cellspacing='0' width='200'>");
                
                // for문을 이용해 1부터 9까지 곱셈 결과 출력
                for (int i = 1; i <= 9; i++) {
                    out.print("<tr>");
                    out.print("<td align='center'>" + dan + " x " + i + " = <b>" + (dan * i) + "</b></td>");
                    out.print("</tr>");
                }
                out.print("</table>");
                
            } catch (NumberFormatException e) {
                // 숫자가 아닌 값이 입력되었을 경우의 예외 처리
                out.print("<p>올바른 숫자를 입력해주세요.</p>");
            }
            out.print("<br><a href='gugudan'>다른 단수 입력하기</a>");
        }

        out.print("</body></html>");
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}