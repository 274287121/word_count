#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request,'home.html')

def count(request):
	total_count=(len(request.GET['text']))
	user_text=request.GET['text']
	type(user_text)
	word_count={}
	for word in user_text:
		if word not in word_count:
			word_count[word]=1
		else:
			word_count[word]+=1

	sorted_dict=sorted(word_count.items(),key=lambda m:m[1],reverse=True)

	return render(request,'count.html',
					{'count':total_count,'user_text':user_text,
					'wordcount':word_count,'sorteddict':sorted_dict})