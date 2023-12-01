#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#define latt 50

struct lista
{
	float posx;
	float posy;
	float posz;
	struct lista *prox;
};

void main(int argc, char *argv[])
{
	FILE *in, *out, *lt;
	struct lista *ini, *aux, *t, *q, *r, *d, *g;
	float x, y, z, dife1, diff1, dife2, diff2, lx, ly, lz, a1, a2, a3, Ox, Oy, Oz, H1x, H1y, H1z, H2x, H2y, H2z, d1, d2, ds1, ds2, dist1, dist2;
        char atom, buff1[60], buff2[60], buff3[60], buff4[60], buff5[60], *arq;
        int step, bead, cont=0, soma, i, to, ta, tb, n_atom;

	ini=aux=NULL;
	arq=argv[1];

	in = fopen(arq, "r");
	out = fopen("dist.dat", "w");

	while(!feof(in))
	{
		cont=0;
                ini=aux=NULL;
                fscanf(in, "%s\t%s\t%d\t%s\t%d\t%s\t%s\n", buff1, buff2, &step, buff3, &bead, buff4, buff5);
                fscanf(in, "%s\t%f\t%f\t%f\t%f\t%f\t%f\t%s\t%d\t%d\n", buff1, &lx, &ly, &lz, &a1, &a2, &a3, buff2, &to, &ta);
		
		for(i=0; i<288; i++)
		{
			fscanf(in, "%s\t%d\t%c\t%d\t%d\t%f\t%f\t%f\t%f\t%f\t%d\n", buff1, &n_atom, &atom, &to, &ta, &x, &y, &z, &a1, &a2, &tb);

			q=(struct lista *)malloc(sizeof(struct lista));
                                q->posx=x;
                                q->posy=y;
                                q->posz=z;
                                q->prox=NULL;

                                if(!ini)
                                        ini=q;
                                else
                                        t->prox=q;
                                t=q;

			
			if(atom=='O')
			{
				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y;
                                g->posz=z;
                                g->prox=NULL;

				
				if(!aux)
					aux=g;
				else
					r->prox=g;
				r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y+ly;
                                g->posz=z+lz;
                                g->prox=NULL;
				r->prox=g;
				r=g;
				
				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y+ly;
                                g->posz=z;
                                g->prox=NULL;
				r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y;
                                g->posz=z;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y+ly;
                                g->posz=z+lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

                                g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y+ly;
                                g->posz=z;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

                                g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y;
                                g->posz=z+lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y;
                                g->posz=z+lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

                                g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y-ly;
                                g->posz=z;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

                                g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y-ly;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

                                g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y;
                                g->posz=z;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

                                g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y-ly;
                                g->posz=z;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y-ly;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y-ly;
                                g->posz=z+lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y+ly;
                                g->posz=z+lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y-ly;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y+ly;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y+ly;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y-ly;
                                g->posz=z+lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y+ly;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x;
                                g->posy=y-ly;
                                g->posz=z+lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y+ly;
                                g->posz=z;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y-ly;
                                g->posz=z;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x+lx;
                                g->posy=y;
                                g->posz=z-lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;

				g=(struct lista *)malloc(sizeof(struct lista));
                                g->posx=x-lx;
                                g->posy=y;
                                g->posz=z+lz;
                                g->prox=NULL;
                                r->prox=g;
                                r=g;
			}
		
		}

		fscanf(in, "%s\n", buff1);

		d=ini;
		while(d)
		{
			r=aux;
			
			Ox = d->posx;
			Oy = d->posy;
			Oz = d->posz;
			
			d=d->prox;

			H1x = d->posx;
			H1y = d->posy;
			H1z = d->posz;
			
			d=d->prox;

			H2x = d->posx;
                        H2y = d->posy;
                        H2z = d->posz;

			ds1 = (Ox-H1x)*(Ox-H1x) + (Oy-H1y)*(Oy-H1y) + (Oz-H1z)*(Oz-H1z);	
			ds2 = (Ox-H2x)*(Ox-H2x) + (Oy-H2y)*(Oy-H2y) + (Oz-H2z)*(Oz-H2z);	

			d1 = sqrt(ds1);
			d2 = sqrt(ds2);


			while(r)
			{
				dife1 = (H1x-r->posx)*(H1x-r->posx) + (H1y-r->posy)*(H1y-r->posy) + (H1z-r->posz)*(H1z-r->posz);
				dife2 = (H2x-r->posx)*(H2x-r->posx) + (H2y-r->posy)*(H2y-r->posy) + (H2z-r->posz)*(H2z-r->posz);
				
				diff1 = sqrt(dife1);
				diff2 = sqrt(dife2);

				dist1 = d1-diff1;
				dist2 = d2-diff2;
				
				if(dist1 != 0)
					fprintf(out, "%f\n", dist1);				
				
				if(dist2 != 0)
					fprintf(out, "%f\n", dist2);				

				r=r->prox;
			}
			d=d->prox;

		}
	}

}
