<!DOCTYPE html>
<html>
<head>
	<title>WEBSOCKET SUBSCRIBER</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- bootstrap css -->
	<link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css">
	<!-- datatables css -->
	<link rel="stylesheet" type="text/css" href="assets/css/dataTables.bootstrap.min.css">
</head>
<body>
	<div class="container">
		<div class="row">
			<div class="col-md-12">
				<center><h1 class="page-header">WEBSOCKET SUBSCRIBER</h1> </center>

				<div class="removeMessages"></div>

				<button class="btn btn-default pull pull-right" data-toggle="modal" data-target="#subscribe" id="subscribeModalBtn">
					<span class="glyphicon glyphicon-plus-sign"></span>	Subscribe
				</button>

				<br /> <br /> <br />
				<!--Datatable-->
				<table class="table" id="tabelData">
					<thead>
						<tr>
							<th width="40">No</th>
							<th>Topik</th>
							<th>Pesan</th>
						</tr>
					</thead>
				</table>
			</div>
		</div>
	</div>

	<!-- add modal -->
	<div class="modal fade" tabindex="-1" role="dialog" id="subscribe">
		<div class="modal-dialog" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
					<h4 class="modal-title"><span class="glyphicon glyphicon-plus-sign"></span> Subscribe</h4>
				</div>

				<form class="form-horizontal" method="POST" id="subscribeForm">
					<div class="modal-body">
						<div class="messages"></div> <!--notifikasi pesan -->
						<div class="form-group">
							<label for="topik" class="col-sm-2 control-label">Topik</label>
							<div class="col-sm-10">
								<input type="text" class="form-control" id="topik" name="topik" placeholder="Topik">
							</div>
						</div>
					</div>
				</form>
				<div class="modal-footer">
					<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
					<button type="button" class="btn btn-primary" onclick="subscribe()">Submit</button>
				</div>
			</div><!-- /.modal-content -->
		</div><!-- /.modal-dialog -->
	</div><!-- /.modal -->
	<!-- /add modal -->
	
	<!-- jquery plugin -->
	<script type="text/javascript" src="assets/js/jquery.js"></script>
	<!-- bootstrap js -->
	<script type="text/javascript" src="assets/js/bootstrap.min.js"></script>
	<!-- datatables js -->
	<script type="text/javascript" src="assets/js/jquery.dataTables.min.js"></script>
	<script type="text/javascript" src="assets/js/dataTables.bootstrap.min.js"></script>
	<!-- include custom index.js -->
	<script type="text/javascript" src="script.js"></script>
</body>
</html>
