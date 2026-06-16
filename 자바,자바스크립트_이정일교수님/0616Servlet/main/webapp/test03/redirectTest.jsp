<%@ page language="java" contentType="text/html; charset=UTF-8"
	import="java.util.*"
    pageEncoding="UTF-8"
    isELIgnored="false"%>
<%@ taglib prefix="c" uri="jakarta.tags.core" %>
<c:set var="contextPath" value="${pageContext.request.contextPath}"/>
<c:url var="url1" value="/test01/member1.jsp">
	<c:param name="id" value="hong"/>
	<c:param name="pwd" value="1234"/>
	<c:param name="name" value="홍길동"/>
	<c:param name="email" value="hong@test.com"/>
</c:url>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> c:url 태그 실습</title>
</head>
<body>
	<c:redirect url="/test01/member1.jsp">
		<c:param name="id" value="${'hong'}"/>
		<c:param name="pwd" value="${'1234'}"/>
		<c:param name="name" value="${'홍길동'}"/>
		<c:param name="email" value="${'hong@test.com'}"/>
	</c:redirect>
</body>
</html>