import numpy as np

 
def subset(arr,n):
	xarr = []
	for i in range(n):
		xarr.append(arr[i])
	while xarr[0] == 0 :
		xarr.pop(0)
	x=len(xarr)
	while xarr[x-1]==0:
		xarr.pop(x-1)
		x = len(xarr)
	return xarr


def check_palindrome_with_1_in_middle(zarr,n):
	x=0
	y=0
	

	if n%2==1:
		mid = int((n-1)/2)
		for i in range(n):
			if zarr[i]==zarr[n-1-i] and zarr[mid]==1:
				if i==n-1:
					return bool(123)
			else: 
				return bool(False)
	elif n%2==0:
		mid = int(n/2)
		darr=[]
		for i in range(n):
			if i!=mid and i!=mid-1:
				darr.append(zarr[i])
		for i in range(len(darr)):
			if darr[i] == darr[len(darr)-1-i]:
				if zarr[mid]==1 or zarr[mid-1] == 1:
					if i==len(darr)-1:
						return bool(123)

			else: 
				return bool(False)
def minswaps(arr,n):
	yarr=[]
	for i in range(n):
		yarr.append(arr[i])

	 
	
	if check_palindrome_with_1_in_middle(yarr,n):
		count0=0
		count1=[]
		score1=0
		if n%2:
			for i in range(n):
				if yarr[i]==1:
					count1.append(count0)
				elif yarr[i]==0:
					count0+=1
			for j in range(len(count1)):
				score1+=count1[j]
			mid=int((len(count1)-1)/2)
			score1=score1-count1[mid]
			print("checkpalindrome odd")
			return score1
		else:
			for i in range(n):
				if yarr[i]==1:
					count1.append(count0)
				elif yarr[i]==0:
					count0+=1
			for j in range(len(count1)):
				score1+=count1[j]
			mid1=int(len(count1)/2)
			mid2 = mid1-1
			mid = int(n/2)
			if yarr[mid]==1 and yarr[mid-1]==0:
				score1=score1-count1[mid1]
				print("checkpalindrome even 0 1")
			elif yarr[mid]==0 and yarr[mid-1]==1:
				score1=score1-count1[mid1]
				print("checkpalindrome even 1 0")
			elif yarr[mid]==1 and yarr[mid-1]==1:
				score1=score1-count1[mid1]-count1[mid2]
				print("checkpalindrome even 1 1")
			return score1
			
	else:
		count0LtR=0
		count0RtL=0
		count1LtR=[]
		count1RtL=[]
		for i in range(n):
			if yarr[i]==1:
				count1LtR.append(count0LtR)
			elif yarr[i]==0:
				count0LtR+=1
		for j in range(n):
			if yarr[n-1-j]==1:
				count1RtL.append(count0RtL)
			elif yarr[n-1-j]==0:
				count0RtL+=1
		scoreLtR=0
		scoreRtL=0
		for k in range(len(count1LtR)):
			scoreLtR+=count1LtR[k]
			scoreRtL+=count1RtL[k]
		if scoreLtR <= scoreRtL:
			print("asymmetric LTR")
			return scoreLtR
		else :
			print("asymmetric RTL")
			return scoreRtL
			
n=int(input())
inputlist = list(map(int,input().strip().split()))
arr = np.array(inputlist)



print (subset(arr,n))
print(minswaps(subset(arr,n),len(subset(arr,n))))
				
				
				
			
