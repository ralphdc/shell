<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>insert renren login infos - bidlust@qq.com</title>

    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim 和 Respond.js 是为了让 IE8 支持 HTML5 元素和媒体查询（media queries）功能 -->
    <!-- 警告：通过 file:// 协议（就是直接将 html 页面拖拽到浏览器中）访问页面时 Respond.js 不起作用 -->
    <!--[if lt IE 9]>
      <script src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>
    <![endif]-->
  </head>

  <?php

  function get_ip() {
    if(getenv('HTTP_CLIENT_IP') && strcasecmp(getenv('HTTP_CLIENT_IP'), 'unknown')) {
        $ip = getenv('HTTP_CLIENT_IP');
    } elseif(getenv('HTTP_X_FORWARDED_FOR') && strcasecmp(getenv('HTTP_X_FORWARDED_FOR'), 'unknown')) {
        $ip = getenv('HTTP_X_FORWARDED_FOR');
    } elseif(getenv('REMOTE_ADDR') && strcasecmp(getenv('REMOTE_ADDR'), 'unknown')) {
        $ip = getenv('REMOTE_ADDR');
    } elseif(isset($_SERVER['REMOTE_ADDR']) && $_SERVER['REMOTE_ADDR'] && strcasecmp($_SERVER['REMOTE_ADDR'], 'unknown')) {
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    $res =  preg_match ( '/[\d\.]{7,15}/', $ip, $matches ) ? $matches [0] : '';
	return $res;
}
	if($_SERVER['REQUEST_METHOD'] == 'POST'){
		$cookie = $_POST['cookie'];
  		$token = $_POST['token'];
  		$rtk = $_POST['rtk'];

  		if (empty($cookie) || empty($token) || empty($rtk))
  		{
  			echo "[Error] parameter is null! - cookie | token | rtk";
  		}else{
  			$mysql_host = getenv("mysql_host") ?? '';
  			$mysql_port = getenv("mysql_port") ?? '';
  			$mysql_user = getenv("mysql_user") ?? '';
  			$mysql_pwd 	= getenv("mysql_pwd") ?? '';
  			$mysql_db	= getenv("mysql_db") ?? '';

  			if(empty($mysql_host) || empty($mysql_port) || empty($mysql_user) || empty($mysql_pwd) || empty($mysql_db))
  			{
  				echo "[Error] connect backend parameters is wrong!";
  			}else{
  				$dsn="$mysql:host=$mysql_host;dbname=$mysql_db";
  				try {
				    $dbh = new PDO($dsn, $mysql_user, $mysql_pwd); //初始化一个PDO对象
				    $dbh = null;
				} catch (PDOException $e) {
				    die ("Error!: " . $e->getMessage() . "<br/>");
				}

				$insert_sql = "insert into token(`cookie`, `token`, `rtk`, `sip`) values (?, ? , ? ,?)";
				$stmt = $pdo->prepare($insert_sql);

				$stmt->bindValue(1,$name);
				$stmt->bindValue(2,$age);
				$stmt->bindValue(3,$name);
				$stmt->bindValue(4,get_ip());

				$stmt->execute();
				$insert_id = $pdo->lastInsertId();

				print_r("insert_id:". $insert_id);
  			}
  		}
	}
  ?>

  <body>
    <h1>人人网爬虫 - 提交登录信息</h1>
    <hr/>
    <div class="row">
    	<div class="col-md-6">
    		<form class="form-horizontal" method="post">
			  <div class="form-group">
			    <label for="cookie" class="col-sm-2 control-label">Cookie:</label>
			    <div class="col-sm-10">
			      <textarea id="cookie" placeholder="cookie" name="cookie" class="form-control" rows="7" style="resize: none"></textarea>
			    </div>
			  </div>
			  <div class="form-group">
			    <label for="token" class="col-sm-2 control-label">token:</label>
			    <div class="col-sm-10">
			      <input type="text" class="form-control" id="token" name="token" placeholder="token">
			    </div>
			  </div>
			  <div class="form-group">
			    <label for="rtk" class="col-sm-2 control-label">rtk:</label>
			    <div class="col-sm-10">
			      <input type="text" class="form-control" id="rtk" name="rtk" placeholder="rtk">
			    </div>
			  </div>
			 
			  <div class="form-group">
			    <div class="col-sm-offset-2 col-sm-10">
			     <button type="submit" class="btn btn-primary">提交</button>
			    </div>
			  </div>
			</form>
    	</div>
    </div>
    
    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js"></script>
  </body>
</html>