package sec04.ex03;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Date;
import java.util.List;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/viewMembers")
public class ViewServlet extends HttpServlet{
	@SuppressWarnings("unchecked")
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
	throws ServletException, IOException{
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		
		// 강제 형변환과 제네릭 경고를 없애기 위해 <MemberVO>를 명시해 주는 것도 좋습니다.
		List<MemberVO> membersList = (List<MemberVO>) request.getAttribute("membersList");
		
		out.print("<html><body>");
		out.print("<table border=1><tr align='center' bgcolor='lightgreen'>");
		out.print("<td>아이디</td><td>비밀번호</td><td>이름</td><td>이메일</td><td>가입일</td><td>삭제</td></tr>");
		
		// 데이터가 정상적으로 넘어왔을 때만 for문을 돌리도록 방어 코드 추가
		if (membersList != null) {
			for (int i = 0; i < membersList.size(); i++) {
				MemberVO memberVO = membersList.get(i);
				String id = memberVO.getId();
				String pwd = memberVO.getPwd();
				String name = memberVO.getName();
				String email = memberVO.getEmail();
				Date joinDate = memberVO.getJoinDate();
				
				out.print("<tr><td>" + id + "</td><td>" + pwd + "</td><td>" + name +
						"</td><td>" + email + "</td><td>" + joinDate + "</td><td>"
						+ "<a href='/pro08/member5?command=delMember&id=" + id
						+ "'>삭제</a></td></tr>");
			}
		} else {
			out.print("<tr><td colspan='6'>등록된 회원이 없습니다.</td></tr>");
		}
		
		out.print("</table>");
		
		// [수정 완료] HTML이 끝나기 전(</body> 위)에 링크가 오도록 수정
		out.print("<br><a href='/pro08/memberForm.html'>새 회원 등록하기</a>");
		out.print("</body></html>");
	}
}