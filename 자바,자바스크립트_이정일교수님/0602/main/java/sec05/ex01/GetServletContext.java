package sec05.ex01;

// [수정 포인트] java.awt.List를 지우고 java.util.List로 변경했습니다!
import java.util.List; 
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import jakarta.servlet.ServletContext;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/cget")
public class GetServletContext extends HttpServlet{
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException{
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		ServletContext context = getServletContext();
		
		// java.util.List를 임포트했으므로 get() 메서드를 정상적으로 사용할 수 있습니다.
		List member = (List)context.getAttribute("member");
		String name = (String)member.get(0);
		int age = (Integer)member.get(1);
		
		out.print("<html><body>");
		out.print(name + "<br>");
		out.print(age + "<br>");
		out.print("</body></html>");
	}
}