 cd /volumeUSB1/usbshare/py/data_online &&
             find . -name '?*.*' -type f -printf '%b.%f\0' |
			           awk -F . -v RS='\0' '
					               {s[$NF] += $1; n[$NF]++}
								               END {for (e in s) printf "%15d %4d %s\n", s[e]*512, n[e], e}' |
											             sort -n | numfmt --to=iec-i --suffix=B
