function cputemp()
{
	$.ajax(
	{
		type: "POST",
		url: "cputemp.py",
		dataType: "html",
		success: function(msg)	{
			document.getElementById('box_cputemp').innerHTML = msg;
		},
	});
	
}
