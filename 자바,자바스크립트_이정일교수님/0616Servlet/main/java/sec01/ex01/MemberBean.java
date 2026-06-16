package sec01.ex01;

import java.util.Date;

public class MemberBean {
	private String id;
	private String pwd;
	private String name;
	private String email;
	private Date joinDate;
	
	// 기본 생성자 (<jsp:useBean> 태그가 객체를 생성할 때 반드시 필요합니다)
	public MemberBean() {
	}
	
	public MemberBean(String id, String pwd, String name, String email) {
		super();
		this.id = id;
		this.pwd = pwd;
		this.name = name;
		this.email = email;
	}
	
	// --- 아래부터 Getter와 Setter 메서드들 ---
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id; // 비어있던 부분 완성
	}

	public String getPwd() {
		return pwd;
	}
	public void setPwd(String pwd) {
		this.pwd = pwd;
	}

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}

	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}

	public Date getJoinDate() {
		return joinDate;
	}
	public void setJoinDate(Date joinDate) {
		this.joinDate = joinDate;
	}
}