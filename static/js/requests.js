/*Send post request */
function sendPostRequest(url, data, contentType, dataType, successCallBack,
		failureCallBack) {
	console.log('Request sent to ' + url);
	$.ajax(url, {
		type : 'POST',
		data : data,
		contentType : contentType,
		dataType : dataType,
		success : function(data, status, xhr) {
			successCallBack(data, status, xhr);

		},
		error : function(jqXhr, textStatus, errorMessage) {
			failureCallBack(jqXhr, textStatus, errorMessage);
		}
	});
}

/* Send multipart request for the data */
function sendMultiPartRequest(url, data, successfulFileUpload,
		failureFileUpload) {
	console.log('Request sent to ' + url);
	$.ajax({
		type : 'POST',
		contentType : false,
		url : url,
		data : data,
		processData : false,
		cache : false,
		success : function(data, status, xhr) {
			successfulFileUpload(data, status, xhr);

		},
		error : function(jqXhr, textStatus, errorMessage) {
			failureFileUpload(jqXhr, textStatus, errorMessage);
		}
	});
}

function sendPostRequestWithJsonType(url, jsonData, successCallBack,
		failureCallBack) {
	sendPostRequest(url, jsonData, "application/json; charset=utf-8", "json",
			successCallBack, failureCallBack);
}

function addParamAndSendMultipartRequest(url, formId, inputId, paramName,
		successfulFileUpload, failureFileUpload) {
	var form = $('#' + formId)[0];
	var file = document.getElementById(inputId);
	
	var data = new FormData(form);
	
	/*
	 * Since we delete the data we have to keep a different reference to track
	 * the keys
	 */
	var formData    = new FormData(form);
	var formKeys    = formData.keys();
	var formEntries = formData.entries();

	/*
	 * Delete all the existing form items from formdata as we don't need to send
	 * all the parameters
	 */
	do {
	  var key = formEntries.next().value;
	  if (typeof key !== 'undefined') {
		  data.delete(key[0]);
	  }
	} while (!formKeys.next().done)
	
	/* Attach only the required file */
	data.append(paramName, file.files[0]);

	sendMultiPartRequest(url, data, successfulFileUpload, failureFileUpload);
}

function sendPostRequestandRecieveZipFile(url, myjson, successFileDownload, failureFileDownload) {
	var loading = new Loading();
	jQuery.ajax({
	    url:url,
	    type:'POST',
	    data: myjson,  
	    contentType: 'application/json', 
	    xhrFields:{
	        responseType: 'blob'
	    },
	    success: function(data, status, xhr){
	    	successFileDownload(data, status, xhr);
	    	loading.out();
	    },
	    error:function(jqXhr, textStatus, errorMessage){
	    	loading.out();
	    	failureFileDownload(jqXhr, textStatus, errorMessage);
	    }
	}); 	
}

function sendGetRequest(url,successFunction, failureFunction) {
	jQuery.ajax({
	    url:url,
	    type:'GET',
	    success: function(data, status, xhr){
	    	successFunction(data, status, xhr);
	    },
	    error:function(jqXhr, textStatus, errorMessage){
	    	failureFunction(jqXhr, textStatus, errorMessage);
	    }
	});
}
