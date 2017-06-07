// global variabel tablePegawai
var tabelData;
var no = 1;

$(document).ready(function() {
	// Disable enter untuk submit topik, harus klik button submit
	$(window).keydown(function(event){
		if(event.keyCode == 13) {
		event.preventDefault();
		return false;
		}
	});

	tabelData = $("#tabelData").DataTable();

	ws = new WebSocket('ws://localhost:8877');

    ws.onmessage = function(evt){
		data = JSON.parse(evt.data);
		if(data['pesan'] != null)
		{
			tabelData.row.add([no, data['topik'], data['pesan']]).draw(false);
			no++;
		}
		else{
			alert(data['status']);
		}
		$("#subscribe").modal('hide');
    }

	$("#subscribeModalBtn").on('click', function() {
		// reset the form
		$("#subscribeForm")[0].reset();
		// remove the error
		$(".form-group").removeClass('has-error').removeClass('has-success');
		$(".text-danger").remove();
		// empty the message div
		$(".messages").html("");
	});
});

function subscribe()
{
	if(validasi())
	{
		var topik = $("#topik").val();
				
		data = {'id': 'sub', 'topik' : topik};
		json_encode = JSON.stringify(data);
		alert(json_encode);
		ws.send(json_encode);
	}
};

function validasi()
{
	$(".text-danger").remove();
	
	var topik = $("#topik").val();
	
	if(topik == "") {
		$("#topik").closest('.form-group').addClass('has-error');
		$("#topik").after('<p class="text-danger">Topik harus diisi</p>');
	} else {
		$("#topik").closest('.form-group').removeClass('has-error');
		$("#topik").closest('.form-group').addClass('has-success');
	}

	if(topik)
	{
		return true;
	}
	return false;
};