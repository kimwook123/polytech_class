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
<title> excapeXml 변환하기</title>
</head>
<body>
	<h2>escapeXml 변환하기</h2>
	<h2>
		<pre>
			<c:out value="&lt;" escapeXml="true"/>
			<c:out value="&lt;" escapeXml="false"/>
			<c:out value="&gt;" escapeXml="true"/>
			<c:out value="&gt;" escapeXml="false"/>
			<c:out value="&amp;" escapeXml="true"/>
			<c:out value="&amp;" escapeXml="false"/>
			<c:out value="&#039;" escapeXml="true"/>
			<c:out value="&#039;" escapeXml="false"/>
			<c:out value="&#034;" escapeXml="true"/>
			<c:out value="&#034;" escapeXml="false"/>
		</pre>
	</h2>
</body>
</html>