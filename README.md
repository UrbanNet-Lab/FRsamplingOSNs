# Fast Representative Sampling in Large-Scale Online Social Networks (OSNs)
# IEEE Access, in press

In this article, we proposed some fast representative sampling methods (adpUNI and adpUNI+N) when dealing with large-scale OSNs, which have significant improvement on sampling efficiency and performance based on the observation of heterogeneous userID space. The key idea of our methods are dividing the entire userID space into several equal-length
intervals, whose sampling probability adaptively adjust with its real time target rate.The contributions of this paper are as
follows:
1) We propose and verify two fast adaptive methods (adpUNI and adpUNI+N) to overcome the defects of UNI which is of low efficiency, this is important for sampling large scale OSNs.
2) The subgraph obtained by our methods is of much higher representativeness and connectivity than UNI, which is more important for practical applications, since eventually we need to give a representative subgraph to end-users.
3) In the paper, we also reveal the relationship of three key concepts involved in all sampling methods: perfect uniformity can ensure an unbiased sampling of nodes, but not necessarily a more representative sampled subgraph.

the above files are all the programs used in the paper, including sampling methods and data processing.
