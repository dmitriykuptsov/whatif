import speedtest


def test():
	s = speedtest.Speedtest(secure=True)
	s.get_servers()
	s.get_best_server()
	s.download()
	s.upload()
	res = s.results.dict()
	return res["download"], res["upload"], res["ping"]


def main():
	with open('file.txt', 'w') as f:
		for i in range(50):
			print('Making test #{}'.format(i+1))
			d, u, p = test()
			f.write('Test #{}\n'.format(i+1))
			f.write('Download: {:.2f} Kb/s\n'.format(d / 1024))
			f.write('Upload: {:.2f} Kb/s\n'.format(u / 1024))
			f.write('Ping: {}\n'.format(p))

if __name__ == '__main__':
    main()
