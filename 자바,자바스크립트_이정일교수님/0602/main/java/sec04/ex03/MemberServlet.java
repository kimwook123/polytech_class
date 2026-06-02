package sec04.ex03;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Date; // 또는 java.sql.Date (VO 클래스에 맞춰 import)

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

// 링크에 적힌 '/pro07/member5'을 바탕으로 맵핑 주소 추가
@WebServlet("/member5")
public class MemberServlet extends HttpServlet {
	
	// GET 요청 처리
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		doHandle(request, response);
	}

	// POST 요청 처리
	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		doHandle(request, response);
	}

	private void doHandle(HttpServletRequest request, HttpServletResponse response)
			throws IOException, ServletException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		
		PrintWriter out = response.getWriter();
		MemberDAO dao = new MemberDAO();

		List memberList = dao.listMembers();
		
		request.setAttribute("memberList", memberList);
		RequestDispatcher dispatch = request.getRequestDispatcher("viewMembers");
		dispatch.forward(request, response);
	}
}