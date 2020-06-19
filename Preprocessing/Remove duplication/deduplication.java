/**
*   The script aims to remove duplicated files within each directory. 
*
*   Environment Requirement: Java 7+, Eclipse
*   Date of Last Modified: 06/19/2020
*   Author: Yingfei(Jeremy) Xiang
*
*/

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.security.MessageDigest;
import java.util.HashMap;

public class deduplication {
	public static void main(String args[]) throws Exception {
		File f1 = new File("~\\test");
		//change path
		for(File dir : f1.listFiles()){
			HashMap h = new HashMap();
			if(dir.isDirectory()){
				
			}
			for(File f:dir.listFiles()){
				String checksum = getMD5Checksum(dir + "//" + f.getName());
				if(!h.containsValue(checksum)){
					h.put(f.getName(), checksum);
				}
				else{
					f.delete();
				}
			
			}
		}
	    
	}


	public static byte[] createChecksum(String filename) throws Exception{
		InputStream fis =  new FileInputStream(filename);

  		byte[] buffer = new byte[1024];
  		MessageDigest complete = MessageDigest.getInstance("MD5");
  		int numRead;
  		do {
  			numRead = fis.read(buffer);
  			if (numRead > 0) {
  				complete.update(buffer, 0, numRead);
  			}
  		} while (numRead != -1);
  		fis.close();
  		return complete.digest();
  	}

	// convert a byte array to a HEX string
	public static String getMD5Checksum(String filename) throws Exception {
		byte[] b = createChecksum(filename);
  		String result = "";
  		for (int i=0; i < b.length; i++) {
  			result += Integer.toString( ( b[i] & 0xff ) + 0x100, 16).substring( 1 );
   		}return result;
	}

}
