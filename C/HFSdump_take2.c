#include <MacTypes.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>

struct HFSPlusVolumeHeader {
    UInt16              signature;
    UInt16              version;
    //UInt32              attributes;
    
    unsigned int reserved : 6;
    unsigned int kHFSVolumeHardwareLockBit : 1;
    unsigned int kHFSVolumeUnmountedBit : 1;
    unsigned int kHFSVolumeSparedBlocksBit : 1;
    unsigned int kHFSVolumeNoCacheRequiredBit : 1;
    unsigned int kHFSBootVolumeInconsistentBit : 1;
    unsigned int kHFSCatalogNodeIDsReusedBit : 1;
    unsigned int kHFSVolumeJournaledBit : 1;
    unsigned int reserved1 : 1; 
    unsigned int kHFSVolumeSoftwareLockBit : 1;
    unsigned int reserved2 : 15;

    UInt32              lastMountedVersion;
    UInt32              journalInfoBlock;
 
    UInt32              createDate;
    UInt32              modifyDate;
    UInt32              backupDate;
    UInt32              checkedDate;
 
    UInt32              fileCount;
    UInt32              folderCount;
 
    UInt32              blockSize;
    UInt32              totalBlocks;
    UInt32              freeBlocks;
 
    UInt32              nextAllocation;
    UInt32              rsrcClumpSize;
    UInt32              dataClumpSize;
    UInt32			    nextCatalogID;
 
    UInt32              writeCount;
    UInt64              encodingsBitmap;
 
    UInt32              finderInfo[8];
};
typedef struct HFSPlusVolumeHeader HFSPlusVolumeHeader;

int main(int argc, char ** argv){
	FILE *fp;
	fp = fopen("volheader.bin","r");

	HFSPlusVolumeHeader volheader;
	fread(&volheader, sizeof(HFSPlusVolumeHeader),1,fp);
    
    char *p = volheader.signature;
    char *l = volheader.lastMountedVersion;

    printf("The raw value of signature is %s\n", &p);
	printf("The raw value of version is %x\n", ntohs(volheader.version));
	printf("The raw value of lastMountedVersion is %s\n", &l);
    printf("\n");
    printf("The directory ID of the blessed folder is %x\n", ntohl(volheader.finderInfo[0]));
    printf("The parent directory ID of the blessed file is %x\n", ntohl(volheader.finderInfo[1]));
    printf("The directory ID of the auto-opened folder is %x\n", ntohl(volheader.finderInfo[2]));
    printf("The directory ID of a legacy Mac OS System folder is %x\n", ntohl(volheader.finderInfo[3]));
    
    printf("The directory ID of a bootable OS X system is %x\n", ntohl(volheader.finderInfo[5]));

    


}