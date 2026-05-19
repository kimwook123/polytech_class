package test20;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // GET 요청: 최초 접속 시 로그인 화면 출력
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html; charset=utf-8");
        PrintWriter out = response.getWriter();

        out.print("<html><head><title>로그인</title></head><body>");
        out.print("<h2>시스템 로그인</h2>");
        out.print("<form method='post' action='login'>"); // 자기 자신(login)에게 POST 방식으로 데이터 전송
        out.print("아이디 : <input type='text' name='userId' required><br><br>");
        out.print("비밀번호 : <input type='password' name='userPwd' required><br><br>");
        out.print("<input type='submit' value='로그인'>");
        out.print("</form>");
        out.print("</body></html>");
    }

    // POST 요청: 폼 제출 시 로그인 로직 처리 및 관리자 화면 출력
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 1. 한글 인코딩 설정
        request.setCharacterEncoding("utf-8");
        response.setContentType("text/html; charset=utf-8");
        PrintWriter out = response.getWriter();

        // 2. 사용자가 입력한 아이디와 비밀번호 가져오기
        String userId = request.getParameter("userId");
        String userPwd = request.getParameter("userPwd");

        // 3. 아이디가 'admin'이고 비밀번호가 '1234'인지 확인 (실무에서는 DB와 연동하여 검사합니다)
        if ("admin".equals(userId) && "1234".equals(userPwd)) {
            // 로그인 성공 - 관리자 화면 출력
            out.print("<html><head><title>관리자 페이지</title></head><body>");
            out.print("<h2>👑 관리자 대시보드</h2>");
            out.print("<p><b>" + userId + "</b>님, 환영합니다. 시스템 관리자 권한으로 접속되었습니다.</p>");
            out.print("<hr>");
            out.print("<h3>[관리자 메뉴]</h3>");
            out.print("<ul>");
            out.print("<li><a href='#'>회원 관리</a></li>");
            out.print("<li><a href='#'>게시판 관리</a></li>");
            out.print("<li><a href='#'>시스템 통계 보기</a></li>");
            out.print("</ul>");
            out.print("<br><a href='login'>로그아웃 (처음으로 돌아가기)</a>");
            out.print("</body></html>");
        } else {
            // 로그인 실패 - 경고창을 띄우고 이전 화면(로그인 폼)으로 돌려보냄
            out.print("<script>");
            out.print("alert('아이디 또는 비밀번호가 일치하지 않습니다.');");
            out.print("history.back();");
            out.print("</script>");
        }
    }
}