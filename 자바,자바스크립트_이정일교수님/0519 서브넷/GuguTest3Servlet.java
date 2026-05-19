package test20;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/guguTest3")
public class GuguTest3Servlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 1. 한글 인코딩 설정
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html; charset=utf-8");

        PrintWriter out = response.getWriter();
        
        // 2. 파라미터 가져오기 (단수)
        String danStr = request.getParameter("dan");

        out.print("<html><head><title>구구단 출력 및 선택</title></head><body>");

        if (danStr != null && !danStr.isEmpty()) {
            try {
                int dan = Integer.parseInt(danStr);
                
                out.print("<h3 align='center'>구구단 " + dan + "단</h3>");
                
                // 선택한 값을 다른 서블릿이나 페이지로 보내기 위해 form 태그 추가
                out.print("<form method='post' action='#'>"); 
                out.print("<table border='1' width='800' align='center'>");
                
                // 테이블 헤더 (항목 이름 표시)
                out.print("<tr bgcolor='#FFFF66'>");
                out.print("<th>단일선택(Radio)</th>");
                out.print("<th>다중선택(Checkbox)</th>");
                out.print("<th>수식</th>");
                out.print("<th>결과</th>");
                out.print("</tr>");
                
                // 구구단 계산 및 행 배경색 교대 출력
                for (int i = 1; i <= 9; i++) {
                    if (i % 2 == 1) { 
                        out.print("<tr bgcolor='#99CCFF'>"); // 홀수 행
                    } else {
                        out.print("<tr bgcolor='#CCFFCC'>"); // 짝수 행
                    }
                    
                    // 1열: 라디오 버튼 (name이 모두 같아야 그룹으로 묶여서 하나만 선택 가능)
                    out.print("<td align='center'><input type='radio' name='radioBtn' value='" + i + "'></td>");
                    
                    // 2열: 체크박스 (다중 선택 가능)
                    out.print("<td align='center'><input type='checkbox' name='checkBtn' value='" + i + "'></td>");
                    
                    // 3열, 4열: 구구단 수식과 결과
                    out.print("<td align='center'>" + dan + " * " + i + "</td>");
                    out.print("<td align='center'>" + (dan * i) + "</td>");
                    out.print("</tr>");
                }
                
                out.print("</table>");
                out.print("<br><div align='center'><input type='submit' value='선택한 값 전송하기'></div>");
                out.print("</form>");
                
            } catch (NumberFormatException e) {
                out.print("<h3 align='center'>올바른 숫자를 입력해주세요.</h3>");
            }
        } else {
            // 단수를 입력받는 폼(Form) 출력 (이전 단계에서 해결한 부분)
            out.print("<h3 align='center'>구구단 출력기</h3>");
            out.print("<div align='center'>");
            out.print("<form method='get' action='guguTest3'>");
            out.print("출력할 단수 : <input type='number' name='dan' min='2' max='9' required> ");
            out.print("<input type='submit' value='출력'>");
            out.print("</form>");
            out.print("</div>");
        }

        out.print("</body></html>");
    }
}