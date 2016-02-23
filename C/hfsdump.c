#include <stdio.h>
#include <stdint.h>
#include <netinet/in.h>

// Structure describing the basic info and attributes of an HFS+ partition
// starts at 1024 bytes into partition 
// There's more to it, but it doesn't really matter for our needs

typedef struct HFSPlusGeneralInfo_Prototype {
	uint16_t	signature; // Should read H+ (HFS+) or HX (HFS+ Case-Sensitive)
	uint16_t	version; 
	uint32_t	attributes;
	uint32_t	lastMountedVersion;
	uint32_t	journalInfoBlock;

	uint64_t	spacer;
	uint32_t	lastBackedUp;
	uint32_t	lastFsck;

} HFSPlusGeneralInfo_Prototype;

typedef struct HFSPlusFinderInfo_Prototype {
	uint32_t	BlessedFolderCNID;
	uint32_t	ParentOfBlessedCNID;
	uint32_t	LegacyBlessedSystemFolder;
	uint32_t	reserved;
	uint32_t	OSXBlessedFolderCNID;
	uint64_t	UniqueVolID;
} HFSPlusFinderInfo_Prototype;

enum AttributesBitMask {
	// attributes are 32 x 1-bit flags in a uint32_t
	// 0-6, 14, 16-31 are reserved for future changes to header format
	isHardwareLocked		= 0x80,
	wasCleanlyUnmounted		= 0x100,
	isVolumeInconsistent	= 0x800,
	isJournaledVolume		= 0x2000,
	isSoftwareLocked		= 0x8000
};

void bin(unsigned n){
	unsigned i;
	for (i = 1 << 31; i > 0; i = i / 2){
		(n & i)? printf("1"): printf("0");
	}
}

int main(int argc, char *argv[]){
	FILE *blockDevice=fopen("./dump.bin","rb");
	
	// grab volume general information
	fseek(blockDevice,1024, SEEK_SET);
	struct HFSPlusGeneralInfo_Prototype Header_GeneralInfo;
	fread(&Header_GeneralInfo, sizeof(HFSPlusGeneralInfo_Prototype),1,blockDevice);

	fseek(blockDevice,1104, SEEK_SET);
	struct HFSPlusFinderInfo_Prototype FinderInfo;
	fread(&FinderInfo, sizeof(HFSPlusFinderInfo_Prototype),1,blockDevice);

	printf("The raw value of signature is %x\n", ntohs(Header_GeneralInfo.signature));
	printf("The raw value of version is %x\n", ntohs(Header_GeneralInfo.version));
	printf("The raw value of attributes is %x\n", Header_GeneralInfo.attributes);
	printf("The raw value of lastMountedVersion is %x\n", ntohl(Header_GeneralInfo.lastMountedVersion));
	printf("The raw value of lastBackedUp is %x\n", ntohl(Header_GeneralInfo.lastBackedUp));
	printf("The raw value of lastFsck is %x\n", ntohl(Header_GeneralInfo.lastFsck));

	uint32_t attributes; 
	attributes = ntohl(Header_GeneralInfo.attributes);
	if(attributes & isJournaledVolume){
		printf("Journaling is on!\n");
	}

	if((attributes & isSoftwareLocked) == 0){
		printf("Software lock is off.\n");
	}
	

	//printf("The raw value of thing is %x\n", Header_GeneralInfo.)
	fclose(blockDevice);



}